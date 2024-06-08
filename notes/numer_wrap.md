# 数字在范围内循环

常用于菜单、队列、动画的光标索引。

## 简单运用
数字在 Index   Index+1   Index+2 之间循环
```
((Index + 1) + 3) % 3
```

## 用于数组
如果是基于 0 开始，就可以省略一次
```
(index + 1) % Array.Width
```

## 用于动画帧
```
(Self.AnimationFrame + 1) % Self.AnimationFrameCount
```

## 拓展：
变量
- Start: 起始位置，可以是 0, -2, 5...
- Total: 共包含多少个选项
- Current 当前选项的位置 `Start + Current`
- Max: 选项最后的位置：`Start + Total -1`
  
## 公式
```
((Current + 1) + Total) % Total
```
