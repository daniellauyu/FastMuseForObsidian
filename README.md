# FastMuseForObsidian

[English](README_EN.md) | [中文](README_ZH.md)

FastMuseForObsidian is an Alfred Workflow designed to help users quickly add inspirations and tasks to their Obsidian journals. This workflow enables seamless recording of important thoughts and tasks, thereby enhancing productivity in both work and personal life.

## Features

- **Quickly Add Inspirations**: Add inspirations directly to your Obsidian journal via Alfred.
- **Manage Tasks**: Quickly add and manage tasks in your Obsidian list.
- **Automatic Journal Management**: Automatically recognizes dates to ensure inspirations and tasks are recorded correctly by date.

## Installation

1. Ensure you have installed Alfred 4 and purchased the [Alfred Powerpack](https://www.alfredapp.com/powerpack/).
2. Ensure your system has Python 3.6 or higher installed. You can download and install it from the [Python official website](https://www.python.org/downloads/).
3. Download the `FastMuseForObsidian.alfredworkflow` file: [Download Here](https://github.com/daniellauyu/FastMuseForObsidian/blob/master/FastMuseForObsidain.alfredworkflow)
4. Double-click the downloaded file to install the Workflow.

## Configuration

Before using the Workflow, you need to set several environment variables to ensure it works properly:

- `BASE_PATH`: Set to the path where your Obsidian journal is stored.
- `DIARY_KEYWORD`: The naming keyword for journal files, default is "Fragment".
- `INSPIRATION_TAG`: Tag for recording inspirations, default is "## Inspiration".
- `TODO_TAG`: Tag for recording To-Do items, default is "To-Do List".

These variables can be configured via the Alfred Workflow settings interface.

## Usage

- **Add Inspirations**: Activate Alfred, type the keyword (e.g., `lg`) followed by your inspiration content, and press Enter to add.
- **Add Tasks**: Activate Alfred, type the keyword (e.g., `td`) followed by the task content, and press Enter to add.

## Support

If you encounter any problems or have suggestions while using FastMuseForObsidian, please submit feedback through [GitHub Issues](https://github.com/daniellauyu/FastMuseForObsidian/issues).

## Copyright Information

FastMuseForObsidian © 2024, published by DANIEL LAU. All rights reserved.

## License

This project is released under the [MIT License](LICENSE).
