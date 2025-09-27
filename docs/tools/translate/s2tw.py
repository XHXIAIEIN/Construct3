#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""中文简繁转换工具"""

import csv
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Iterator, List, Dict, Any

if sys.platform.startswith('win'):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 标点转换规则常量
PUNCTUATION_RULES = [
    (r'([\u4e00-\u9fff])[?]$', r'\1？'),      # 句末问号
    (r'([\u4e00-\u9fff])[!]$', r'\1！'),      # 句末感叹号
    (r'([\u4e00-\u9fff])\.(?=\s|$)', r'\1。') # 句号
]

# 保护模式（避免转换）
PROTECTED_PATTERN = re.compile(r'''
    \[[a-zA-Z/][^\]]*\] |           # BBCode
    \{[^}]*\} |                     # 占位符
    [a-zA-Z]+\.[a-zA-Z]+ |          # 域名/属性
    [{}[\]<>] |                     # 特殊符号
    ^\s*[a-zA-Z]+ |                 # 英文开头
    [a-zA-Z]+:\s*[a-zA-Z]+ |        # 键值对
    https?:// |                     # URL
    \b\d+°\b |                      # 角度符号
    ""                              # CSV转义引号
''', re.VERBOSE)


class Config:
    DEFAULTS = {
        'input_file': 'zh-CN.csv',           # 输入CSV文件路径
        'output_file': 'zh-TW.csv',          # 输出CSV文件路径
        'column_index': 1,                   # 要转换的列索引（0为第一列）
        'start_row': 0,                      # 起始行数（0为从第一行开始）
        'limit': 0,                          # 最大处理行数（0为不限制）
        'batch_size': 500,                  # 批次大小，每N行显示进度报告

        'converter_engine': 'opencc',        # 转换引擎: opencc, zhconv
        'opencc_config': ['s2t', 't2tw'],    # OpenCC转换配置(支持多步转换)
        'zhconv_target': 'zh-tw',            # zhconv目标地区 
        'custom_dict': 'custom_dict.json',   # 自定义词库文件路径
        'custom_dict_columns': [0, 5],       # 自定义词库匹配列索引列表
        'punctuation_convert': True,         # 是否转换标点符号
        'progress_file': 'progress.json'     # 断点续传进度文件路径
    }
    
    def __init__(self, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        
        self.input_file = Path(config['input_file'])
        self.output_file = Path(config['output_file'])
        self.column_index = config['column_index']
        self.start_row = config['start_row']
        self.limit = config['limit']
        self.batch_size = config['batch_size']
        
        self.converter_engine = config['converter_engine']
        self.opencc_config = config['opencc_config']
        self.zhconv_target = config['zhconv_target']
        self.punctuation_convert = config['punctuation_convert']
        self.custom_dict = config['custom_dict']
        self.custom_dict_columns = config['custom_dict_columns']
        self.progress_file = Path(config['progress_file'])


class ConversionEngine:
    def __init__(self, engine: str, **config):
        self.engine = engine
        self.config = config
        self._converter = None
        self._init_engine()
        
    def _init_engine(self):
        if self.engine == 'opencc':
            try:
                import opencc
                opencc_config = self.config.get('opencc_config', ['s2t', 't2tw'])
                
                # 支持多步转换
                if isinstance(opencc_config, list):
                    self._converters = [opencc.OpenCC(config) for config in opencc_config]
                    config_display = ' → '.join(opencc_config)
                else:
                    self._converters = [opencc.OpenCC(opencc_config)]
                    config_display = opencc_config
                    
                print(f"引擎: OpenCC ({config_display})")
            except ImportError:
                print("警告: OpenCC未安装，尝试使用zhconv")
                self.engine = 'zhconv'
                self._init_engine()
                
        elif self.engine == 'zhconv':
            try:
                import zhconv
                self._converter = zhconv
                target = self.config.get('zhconv_target', 'zh-tw')
                print(f"引擎: zhconv ({target})")
            except ImportError:
                print("错误: zhconv未安装，请运行 pip install zhconv")
                raise ImportError("zhconv库未安装")
    
    def convert(self, text: str) -> str:
        if not text or not text.strip():
            return text
            
        if self.engine == 'opencc':
            # 支持多步转换
            result = text
            for converter in self._converters:
                result = converter.convert(result)
            return result
        elif self.engine == 'zhconv':
            return self._converter.convert(text, self.config.get('zhconv_target', 'zh-tw'))
        else:
            return text


def _convert_punctuation(text: str) -> str:
    """保守的标点符号转换，避免破坏BBCode、占位符和CSV转义"""
    # 早期退出条件
    if not text or not text.strip():
        return text
    
    # 跳过英文内容过多的文本
    ascii_ratio = sum(1 for c in text if ord(c) < 128) / len(text)
    if ascii_ratio > 0.5:
        return text
    
    # 检查保护模式
    if PROTECTED_PATTERN.search(text):
        return text
    
    # 应用标点转换规则
    result = text
    for pattern, replacement in PUNCTUATION_RULES:
        result = re.sub(pattern, replacement, result)
    
    # 引号转换
    return _convert_quotes(result)


def _convert_quotes(text: str) -> str:
    """转换引号为中文引号「」"""
    # 检测需要转换的引号类型
    quote_chars = ["'", "'", "'", '"', """, """]
    if not any(c in text for c in quote_chars):
        return text
    
    # 统一转换各种引号为标准英文引号便于处理
    replacements = {
        "'": "'", "'": "'",     # 中文单引号转英文
        """: '"', """: '"',     # 中文双引号转英文
    }
    
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    
    # 转换引号为中文引号「」
    chars = list(text)
    quote_stack = []  # 用栈来跟踪引号配对
    
    for i, char in enumerate(chars):
        if char in ["'", '"']:
            # 判断是开引号还是闭引号
            prev_char = chars[i-1] if i > 0 else ' '
            next_char = chars[i+1] if i < len(chars) - 1 else ' '
            
            # 判断引号类型的逻辑
            is_opening = (
                i == 0 or                                    # 行首
                prev_char in ' \t\n([{' or                   # 前面是空白或开括号
                ('\u4e00' <= prev_char <= '\u9fff' and      # 前面是中文且后面不是空白
                 next_char != ' ')
            )
            
            # 如果栈为空或者明显是开引号，则为开引号
            if not quote_stack or is_opening:
                chars[i] = '「'
                quote_stack.append(i)
            else:
                # 否则为闭引号
                chars[i] = '」'
                if quote_stack:
                    quote_stack.pop()
    
    return ''.join(chars)


class ProgressTracker:
    def __init__(self, progress_file: Path, output_file: Path):
        self.progress_file = progress_file
        self.output_file = output_file
        
    def load(self) -> int:
        if not self.progress_file.exists():
            return -1
        try:
            with open(self.progress_file) as f:
                data = json.load(f)
            if data.get('output_file') == str(self.output_file):
                return data.get('last_row', -1)
        except (json.JSONDecodeError, OSError):
            return -1
        return -1
        
    def save(self, row_num: int):
        try:
            with open(self.progress_file, 'w') as f:
                json.dump({
                    'output_file': str(self.output_file),
                    'last_row': row_num,
                    'timestamp': datetime.now().isoformat()
                }, f)
        except OSError:
            pass
            
    def clear(self):
        try:
            self.progress_file.unlink(missing_ok=True)
        except OSError:
            pass


UI_CONFIG = {
    'bar_width': 20,          # 进度条字符数量 [████████░░░░]
    'preview_length': 24,     # 文本预览显示字符数量
    'separator_width': 85,    # 分隔线总宽度
    'timestamp_width': 8,     # 时间列宽度 "14:30:26"
    'progress_width': 30,     # 进度列宽度
    'original_width': 35      # 原文列宽度
}

def show_progress(current: int, limit: int, original: str, converted: str):
    timestamp = datetime.now().strftime('%H:%M:%S')
    progress_info = _format_progress(current, limit)
    original_col = _pad_text(_truncate_text(original), UI_CONFIG['original_width'])
    result_text = _truncate_text(converted) if converted != original else "(无变化)"
    
    print(f"{timestamp:<8} {progress_info:<29} {original_col} | {result_text}")

def _format_progress(current: int, limit: int) -> str:
    """格式化进度信息"""
    if limit > 0:
        percent = (current / limit) * 100
        filled = int(percent / 100 * UI_CONFIG['bar_width'])
        bar = '█' * filled + '░' * (UI_CONFIG['bar_width'] - filled)
        return f"[{bar}] {percent:5.1f}%"
    return f"#{current}"

def _char_width(char: str) -> int:
    """计算单个字符的显示宽度"""
    eaw = unicodedata.east_asian_width(char)
    return 2 if eaw in ('F', 'W') else 1

def _display_width(text: str) -> int:
    """计算文本的显示宽度"""
    return sum(_char_width(char) for char in text)

def _truncate_text(text: str) -> str:
    """按显示宽度截断文本"""
    max_width = UI_CONFIG['preview_length']
    if _display_width(text) <= max_width:
        return text
        
    result = []
    current_width = 0
    
    for char in text:
        char_width = _char_width(char)
        if current_width + char_width > max_width:
            if current_width + 1 <= max_width:
                result.append('…')
            break
        result.append(char)
        current_width += char_width
    
    return ''.join(result)

def _pad_text(text: str, target_width: int) -> str:
    """根据显示宽度对齐文本"""
    current_width = _display_width(text)
    if current_width >= target_width:
        return text
    padding = target_width - current_width
    return text + ' ' * padding


def show_final_report(stats: Dict[str, Any], output_file: Path):
    elapsed = datetime.now() - stats['start_time']
    success_rate = 100.0 if stats['processed'] == 0 else ((stats['processed'] - stats['errors']) / stats['processed']) * 100
    separator = "=" * UI_CONFIG['separator_width']
    
    print(f"\n{separator}")
    print("处理完成")
    print(f"{separator}")
    print(f"总计: {stats['processed']} 行")
    print(f"成功: {success_rate:.1f}%")
    print(f"用时: {str(elapsed).split('.')[0]}")
    
    if stats['custom_applied'] > 0:
        print(f"词库: {stats['custom_applied']} 次应用")
    if stats['errors'] > 0:
        print(f"错误: {stats['errors']} 行失败")
        
    print(f"输出: {output_file}")
    print(f"{separator}")


class Converter:
    def __init__(self, **kwargs):
        self.config = Config(**kwargs)
        self.progress = ProgressTracker(self.config.progress_file, self.config.output_file)
        
        # 初始化转换引擎
        self.engine = ConversionEngine(
            self.config.converter_engine,
            opencc_config=self.config.opencc_config,
            zhconv_target=self.config.zhconv_target
        )
        
        self.custom_rules = self._load_custom_dict()
        self.stats = {'processed': 0, 'errors': 0, 'custom_applied': 0, 'start_time': None}
        
    def _load_custom_dict(self) -> list:
        try:
            with open(self.config.custom_dict, 'r', encoding='utf-8') as f:
                rules = json.load(f)
            
            # 验证规则格式并过滤无效规则
            valid_rules = [rule for rule in rules if len(rule) == 3]
            invalid_count = len(rules) - len(valid_rules)
            
            print(f"词库: {len(valid_rules)} 条规则" + 
                  (f" ({invalid_count} 条无效)" if invalid_count else ""))
            return valid_rules
            
        except FileNotFoundError:
            print("词库: 未找到文件")
            return []
        except (json.JSONDecodeError, TypeError) as e:
            print(f"词库: 格式错误 ({type(e).__name__})")
            return []
        except Exception as e:
            print(f"词库: 加载失败 ({type(e).__name__})")
            return []
    
    def _apply_custom_rules(self, text: str, full_row: List[str]) -> str:
        if not self.custom_rules or not text:
            return text
            
        result = text
        applied_count = 0
        
        for original, replacement, context in self.custom_rules:
            if original in result and self._match_context(full_row, context):
                result = result.replace(original, replacement)
                applied_count += 1
        
        self.stats['custom_applied'] += applied_count
        return result
    
    def _match_context(self, full_row: List[str], context: str) -> bool:
        if not context.strip():
            return True
        
        # 在指定的列中搜索上下文
        search_columns = self.config.custom_dict_columns
        search_texts = []
        
        for col_index in search_columns:
            if col_index < len(full_row):
                search_texts.append(full_row[col_index])
        
        # 如果指定列为空，则回退到全行搜索
        if not search_texts:
            search_text = ','.join(full_row)
        else:
            search_text = ','.join(search_texts)
            
        return any(term in search_text for term in context.strip().split())
            
    def _process_row(self, row: List[str]) -> tuple:
        if len(row) <= self.config.column_index or not row[self.config.column_index].strip():
            return row, '', ''
            
        original = row[self.config.column_index]
        try:
            # 使用转换引擎
            converted = self.engine.convert(original)
            
            # 应用自定义词库规则
            final_result = self._apply_custom_rules(converted, row)
            
            # 标点符号转换
            if self.config.punctuation_convert:
                final_result = _convert_punctuation(final_result)
            
            row[self.config.column_index] = final_result
            return row, original, final_result
        except Exception:
            self.stats['errors'] += 1
            return row, original, original
                
    def run(self):
        if not self.config.input_file.exists():
            print(f"错误: 文件不存在 {self.config.input_file}")
            return
        
        self._print_header()
        resume_row = self.progress.load()
        actual_start_row = max(self.config.start_row, resume_row + 1 if resume_row >= 0 else self.config.start_row)
        self._print_start_info(resume_row, actual_start_row)
        
        self.stats['start_time'] = datetime.now()
        print(f"\n开始处理 {self.stats['start_time'].strftime('%H:%M:%S')}")
        self._print_progress_header()
        print("-" * UI_CONFIG['separator_width'])
        
        self._process_files(resume_row, actual_start_row)
    
    def _print_progress_header(self):
        header_original = _pad_text('原文', UI_CONFIG['original_width'])
        if self.config.limit > 0:
            print(f"{'时间':<8} {'进度':<29} {header_original} | 转换结果")
        else:
            print(f"{'时间':<8} {'行号':<29} {header_original} | 转换结果")
        
    def _print_header(self):
        limit_text = f"{self.config.limit}行" if self.config.limit > 0 else "全部"
        print(f"\n转换任务")
        print(f"输入: {self.config.input_file}")
        print(f"输出: {self.config.output_file}")  
        print(f"范围: {limit_text} | 列: {self.config.column_index}")
        
    def _print_start_info(self, resume_row: int, actual_start_row: int):
        """打印启动信息"""
        info_items = []
        
        if self.config.start_row > 0:
            info_items.append(f"起始: 第{self.config.start_row + 1}行")
        if resume_row >= 0:
            info_items.append(f"续传: 第{resume_row + 1}行")
        if actual_start_row != self.config.start_row:
            info_items.append(f"实际: 第{actual_start_row + 1}行")
        
        for info in info_items:
            print(info)
        
    def _process_files(self, resume_row: int, actual_start_row: int):
        """处理文件转换"""
        mode = 'a' if resume_row >= 0 else 'w'
        processed = 0
        
        with open(self.config.output_file, mode, encoding='utf-8', newline='') as outf:
            writer = csv.writer(outf)
            processed = self._process_csv_rows(writer, actual_start_row, processed)
        
        show_final_report(self.stats, self.config.output_file)
        self.progress.clear()
    
    def _process_csv_rows(self, writer, actual_start_row: int, processed: int) -> int:
        """处理CSV行数据"""
        with open(self.config.input_file, 'r', encoding='utf-8') as inf:
            reader = csv.reader(inf)
            for row_num, row in enumerate(reader):
                if self._should_stop_processing(processed, row_num, actual_start_row):
                    if processed >= self.config.limit > 0:
                        break
                    continue
                
                processed = self._handle_row(writer, row, row_num, processed)
        return processed
    
    def _should_stop_processing(self, processed: int, row_num: int, actual_start_row: int) -> bool:
        """判断是否应该停止处理"""
        return (self.config.limit > 0 and processed >= self.config.limit) or row_num < actual_start_row
    
    def _handle_row(self, writer, row: List[str], row_num: int, processed: int) -> int:
        """处理单行数据并返回更新的processed计数"""
        new_row, original, converted = self._process_row(row)
        writer.writerow(new_row)
        self.progress.save(row_num)
        
        if not original:
            return processed
            
        processed += 1
        self.stats['processed'] += 1
        show_progress(processed, self.config.limit, original, converted)
        
        if processed % self.config.batch_size == 0:
            self._show_batch_report(processed)
            
        return processed
    
    def _show_batch_report(self, processed: int):
        elapsed = datetime.now() - self.stats['start_time']
        success_rate = 100.0 if self.stats['processed'] == 0 else ((self.stats['processed'] - self.stats['errors']) / self.stats['processed']) * 100
        
        print(f"\n进度检查点 - {processed} 行")
        if self.config.limit > 0:
            print(f"完成: {processed}/{self.config.limit} ({processed/self.config.limit*100:.1f}%)")
        print(f"成功率: {success_rate:.1f}% | 用时: {str(elapsed).split('.')[0]}")
        print("-" * UI_CONFIG['separator_width'])


def main(config=None):
    converter = Converter(**(config or {}))
    converter.run()


if __name__ == "__main__":
    main()
