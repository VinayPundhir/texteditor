# Text Editor

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/VinayPundhir/texteditor/blob/main/LICENSE)

A simple text editor application that allows you to save, read, write, and edit text files.

## Features

- Create new text files
- Open and edit existing text files
- Save changes to text files
- Read the contents of text files

## Installation

1. Clone the repository:

```bash
git clone https://github.com/VinayPundhir/texteditor.git
```

2. Navigate to the project directory:
   ```bash
   cd texteditor
   ```
   
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ``` 

# Run
To run the text editor, use the following command:

```bash
python main.py
```

This will start the application and open the main text editor window.

# Packaging
If you want to package your application for distribution, you can use tools like PyInstaller or cx_Freeze to create an executable file.

For example, with PyInstaller, you can use the following command to create a standalone executable:

```bash
pyinstaller --onefile main.py
```

This will generate a single executable file in the dist directory, which can be distributed and run on other machines without the need for Python or any dependencies.

Please note that the packaging process may vary depending on your specific requirements and target platform. Refer to the documentation of the packaging tool you choose for more details.

Remember to customize these instructions based on your specific project structure and requirements.
