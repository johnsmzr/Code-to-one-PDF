# Code to PDF Converter [中文](Chinese-README.md)

**Code to PDF Converter** is a Python tool for converting source code files within a directory into a single PDF document, while allowing you to specify files and directories to exclude through a configuration file. This tool is particularly useful for developers who need to archive or share their code repositories in a print-friendly format.

## Features

- Convert all source code files within a directory into a single PDF file.
- Exclude specific files and directories using a configuration file.
- Support custom file patterns using wildcards in the configuration.

## Installation

To use this tool, you need to have Python installed on your system. Clone this repository and install the required dependencies:

```bash
git clone git@github.com:johnsmzr/Code-to-one-PDF.git 
cd Code-to-one-PDF 
pip install -r requirements.txt
```

## Usage

Copy the compiled binary to the directory containing the code you want to convert to PDF, and run it:

```bash
./code-to-pdf
```

(Or manually run the Python code)

## Configuration File

The configuration file `.pdfignore.yml` should be placed in the same directory. It specifies which files and directories to exclude. For example:

```yaml
directories:
  - .git
  - log
files:
  - .DS_Store
patterns:
  - '*.pdf'
  - '*.tmp'

```


## Compile to Binary

```bash
pyinstaller --onefile code-to-pdf.py
```

## FAQ

**Q: Can I exclude files based on their content?**

**A: Currently, exclusion is only based on file names and directory paths specified in the configuration file.**