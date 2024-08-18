# FastMuseForObsidian

[English](README_EN.md) | [中文](README.md)

FastMuseForObsidian 是一个 Alfred Workflow，旨在帮助用户快速将灵感和待办事项添加到 Obsidian 日记中。通过此 Workflow，用户可以无缝地记录重要的思考和任务，从而提高工作和生活效率。

## 功能

- **快速添加灵感**：直接通过 Alfred 添加灵感到你的 Obsidian 日记。
- **管理待办事项**：快速添加和管理 Obsidian 中的待办事项列表。
- **自动日记管理**：自动识别日期，确保灵感和待办事项按日期正确记录。

## 安装

1. 确保你已经安装了 Alfred 4 并购买了 [Alfred Powerpack](https://www.alfredapp.com/powerpack/)。
2. 确保你的系统中安装了 Python 3.6 或更高版本。你可以从 [Python 官网](https://www.python.org/downloads/) 下载并安装。
3. 下载 `FastMuseForObsidian.alfredworkflow` 文件：[下载](https://github.com/daniellauyu/FastMuseForObsidian/blob/master/FastMuseForObsidain.alfredworkflow)

4. 双击下载的文件以安装 Workflow。

## 配置

在使用 Workflow 前，你需要设置几个环境变量以确保它能正常工作：

- `BASE_PATH`：设置为你的 Obsidian 日记存储的路径。
- `DIARY_KEYWORD`：日记文件的命名关键词，默认为“碎片”。
- `INSPIRATION_TAG`：用于灵感记录的标签，默认为“## 灵感”。
- `TODO_TAG`: 用于 Todo 记录的标签，默认为"To-Do List"。

通过 Alfred 的 Workflow 设置界面可以配置这些环境变量。

## 使用方法

- **添加灵感**：激活 Alfred，输入关键词（例如 `lg`）后跟你的灵感内容，按回车添加。
- **添加待办事项**：激活 Alfred，输入关键词（例如 `td`）后跟待办内容，按回车添加。

> 关键词可根据自己使用习惯自定义。

## 支持

如果你在使用 FastMuseForObsidian 时遇到任何问题或有任何建议，请通过 [GitHub Issues](https://github.com/daniellauyu/FastMuseForObsidian/issues) 提交反馈。

## 版权信息

FastMuseForObsidian © 2024, 由 DANIEL LAU 发布。所有权利保留。

## 许可

本项目采用 [MIT 许可证](LICENSE) 发布。
