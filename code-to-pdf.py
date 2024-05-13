import fnmatch
import os

import yaml
from fpdf import FPDF

# Load the blacklist from the .code2pdf file
blacklist_file = ".pdfignore.yml"
if os.path.exists(blacklist_file):
    with open(blacklist_file, "r") as f:
        blacklist = yaml.safe_load(f)
else:
    blacklist = {"directories": [], "files": [], "patterns": []}

# Define file extensions to consider as code files
code_extensions = [
    ".py",
    ".js",
    ".html",
    ".css",
    ".php",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".cs",
    ".rb",
    ".pl",
    ".sh",
    ".sql",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".md",
    ".rst",
    ".txt",
]

# Create a new PDF object
pdf = FPDF()


# Function to add a file to the PDF
def add_file_to_pdf(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        for line in content.split("\n"):
            # pdf.add_font('courier', '', 'courier.ttf', uni=True)
            # pdf.add_font('Courier', '', None, uni=True)
            pdf.set_font("Courier", "", 10)
            line = line.encode("latin-1", "replace").decode("latin-1")
            pdf.cell(0, 5, txt=line, ln=1)


# Iterate over all files and directories in the current directory
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in blacklist["directories"]]
    for file in files:
        if (
            file not in blacklist["files"]
            and os.path.splitext(file)[1].lower() in code_extensions
            and not any(
                fnmatch.fnmatch(file, pattern) for pattern in blacklist["patterns"]
            )
        ):
            file_path = os.path.join(root, file)
            pdf.add_page()
            pdf.set_font("courier", "B", 16)
            pdf.cell(0, 10, txt=file_path, ln=1)
            add_file_to_pdf(file_path)

# Save the PDF file
pdf.output("code.pdf", "F")
print("Code files have been converted to code.pdf")