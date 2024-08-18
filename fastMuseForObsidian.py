#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：FormulaDesign 
@Software : PyCharm
@File ：fastMuseForObsidian.py
@Author ：daniel lau
@Date ：2024/8/18 00:21
@site : www.liuyude.com
@describe : 通过alfred快速在obsidain中插入灵感记录
"""

import sys
import datetime

# 接收从Alfred传入的参数
input_text = sys.argv[1] if len(sys.argv) > 1 else "默认文本"

# 设置文件目录和名称格式
base_path = "/Users/daniellau/SynologyDrive/obsidian_nas/6-每日记录"
date_today = datetime.datetime.now().strftime("%Y%m%d")  # 格式化日期
file_name = f"碎片-{date_today}.md"

# 完整的文件路径
full_path = f"{base_path}/{file_name}"

# 获取当前时间戳
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 格式化要添加的文本，包含从Alfred传入的参数
text_to_add = f"- {timestamp} {input_text}\n"

# 读取并修改文件内容
try:
    with open(full_path, 'r+', encoding='utf-8') as file:
        content = file.readlines()
        inspiration_index = next(i for i, line in enumerate(content) if '## 灵感' in line)
        content.insert(inspiration_index + 1, text_to_add)  # 在灵感标题下方插入
        file.seek(0)  # 回到文件开始
        file.writelines(content)  # 写入修改后的内容
        file.truncate()  # 移除旧内容中未被覆盖的部分
    print("灵感已成功添加！")
except FileNotFoundError:
    print("文件未找到，请检查文件路径和名称是否正确。")
except Exception as e:
    print(f"发生错误：{e}")