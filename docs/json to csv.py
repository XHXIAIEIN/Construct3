import json
import csv

# 加载 JSON 数据
file_path = 'data.json'  # 确保 data.json 文件和脚本文件在同一目录下
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 准备 CSV 数据
csv_data = []

# 遍历 JSON 数据中的 "example" 部分
for section, categories in data["example"].items():
    for category, category_data in categories.items():
        for item in category_data["data"]:
            tags = [category] + item["tags"]  # 将分类内容与标签内容合并
            csv_row = {
                "名称": item["title"],
                "分类": item["category"],
                "作者": ", ".join(item["authors"]),
                "链接": item["link"],
                "标签": ", ".join(tags),
                "内容": ", ".join(item["related_links"])
            }
            csv_data.append(csv_row)

# 定义 CSV 文件路径
csv_file_path = 'example_data.csv'

# 写入 CSV 文件
with open(csv_file_path, 'w', encoding='utf-8-sig', newline='') as csvfile:
    fieldnames = ["名称", "分类", "作者", "链接", "标签", "内容"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(csv_data)

print(f"CSV file saved to {csv_file_path}")
