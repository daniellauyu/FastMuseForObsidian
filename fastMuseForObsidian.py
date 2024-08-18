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
import os
import datetime

class JournalEntry:
    def __init__(self):
        # 从环境变量中获取配置
        self.base_path = os.getenv('BASE_PATH', '/default/path/if/not/set')
        self.inspiration_tag = os.getenv('INSPIRATION_TAG', '## 插入关键字')
        self.diary_keyword = os.getenv('DIARY_KEYWORD', '日记关键词')

        self.date_today = datetime.datetime.now().strftime("%Y%m%d")
        self.file_name = f"{self.diary_keyword}-{self.date_today}.md"
        self.full_path = f"{self.base_path}/{self.file_name}"
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_inspiration(self):
        input_text = sys.argv[1] if len(sys.argv) > 1 else "默认文本"
        text_to_add = f"- {self.timestamp} {input_text}\n"

        try:
            with open(self.full_path, 'r+', encoding='utf-8') as file:
                content = file.readlines()
                inspiration_index = next(i for i, line in enumerate(content) if self.inspiration_tag in line)
                content.insert(inspiration_index + 1, text_to_add)  # 在灵感标题下方插入
                file.seek(0)  # 回到文件开始
                file.writelines(content)  # 写入修改后的内容
                file.truncate()  # 移除旧内容中未被覆盖的部分
            print("灵感已成功添加！")
        except FileNotFoundError:
            print("文件未找到，请检查文件路径和名称是否正确。")
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    journal_entry = JournalEntry()
    journal_entry.add_inspiration()