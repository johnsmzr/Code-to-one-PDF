  

---

# Code to PDF Converter 代码转换成PDF工具

**代码转换成 PDF 工具** 是一个 Python 工具，用于将目录中的源代码文件转换为单个 PDF 文档，同时可以通过配置文件指定排除某些文件和目录。该工具对需要以打印友好格式存档或给**AI**发送代码库。

## Features 功能

-  将一个目录下的所有源代码文件转换成一个 PDF 文件。
-  使用配置文件排除特定的文件和目录。
-  通过配置中的通配符模式支持自定义文件模式。

## Installation 安装指南

要使用此工具，您需要在系统上安装 Python。克隆此仓库并安装所需的依赖项：

```bash
git clone git@github.com:johnsmzr/Code-to-one-PDF.git
cd Code-to-one-PDF
pip install -r requirements.txt
```

## Usage 使用说明

把编译好的二进制文件复制到需要转PDF的代码的目录下，运行即可：

```bash
./code-to-pdf
```

（或者手动运行 pytho 代码）


## Configuration File 配置文件说明

配置文件 `.pdfignore.yml` 应放置在相同目录中。它指定了要排除哪些文件和目录。例如：

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

## 编译成二进制文件

```bash
pyinstaller --onefile code-to-pdf.py
```

## FAQ 常见问题解答

**Q: 我可以根据文件内容排除文件吗？** 

**A: 目前，排除仅基于配置文件中指定的文件名和目录路径。**

---