#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fastMuseForObsidian 
@Software : PyCharm
@File ：timeLog.py
@Author ：daniel lau
@Date ：2024/8/19 09:32
@site : www.liuyude.com
@describe : 增加时间记录功能，可通过tl参数快速的记录现在正在做什么，用于一天回顾
"""

import sys
import os
import datetime


class JournalEntry:
    def __init__(self):
        # 从环境变量中获取配置
        self.base_path = os.getenv('TIME_LOG_PATH', '/default/path/if/not/set')
        self.diary_keyword = os.getenv('TIME_LOG_TAG', '碎片')

        self.date_today = datetime.datetime.now().strftime("%Y年%m月%d日")
        self.file_name = f"{self.diary_keyword}.md"
        self.full_path = os.path.join(self.base_path, self.file_name)
        self.timestamp = datetime.datetime.now().strftime("%H:%M")

        # 打印初始化信息
        print(f"Initialized JournalEntry with:")
        print(f"  Base path: {self.base_path}")
        print(f"  Diary keyword: {self.diary_keyword}")
        print(f"  Date today: {self.date_today}")
        print(f"  File name: {self.file_name}")
        print(f"  Full path: {self.full_path}")
        print(f"  Timestamp: {self.timestamp}")

    def add_activity(self, activity_type, activity_description):
        # 格式化文本以包括活动类型和描述
        text_to_add = f"\n- {self.date_today} {self.timestamp} 【{activity_type}】 {activity_description}"
        print(f"Adding to journal:")
        print(text_to_add)

        try:
            with open(self.full_path, 'a', encoding='utf-8') as file:
                file.write(text_to_add)
            print("Activity successfully recorded!")
        except FileNotFoundError:
            print("Journal file not found. Please check the path and file name.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        activity_type = sys.argv[1]  # 从 {query} 获取的活动类型
        activity_description = sys.argv[2]  # 从 {var:activity_description} 获取的活动描述
        print(f"Activity Type: {activity_type}, Activity Description: {activity_description}")

        journal_entry = JournalEntry()
        journal_entry.add_activity(activity_type, activity_description)
    else:
        print("Both activity type and description are required.")