import fnmatch
import os

import markdown
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def load_exclusions(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    excluded_dirs = set(config.get("directories", []))
    excluded_files = set(config.get("files", []))
    excluded_patterns = config.get("patterns", [])
    return excluded_dirs, excluded_files, excluded_patterns


def generate_pdf(source_folder, output_pdf, config_path):
    excluded_dirs, excluded_files, excluded_patterns = load_exclusions(config_path)
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    code_style = ParagraphStyle(
        "Code",
        parent=styles["Normal"],
        fontName="STSong-Light",
        fontSize=10,
        leading=12,
    )

    for root, dirs, files in os.walk(source_folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename not in excluded_files and not any(
                fnmatch.fnmatch(filepath, os.path.join(source_folder, pattern))
                for pattern in excluded_patterns
            ):
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
                    if filename.endswith(".md"):
                        html = markdown.markdown(content)
                        content = html

                    story.append(Paragraph(f"File: {filename}", styles["Title"]))
                    for line in content.splitlines():
                        story.append(Paragraph(line.replace(" ", "&nbsp;"), code_style))
                    story.append(Spacer(1, 12))

    doc.build(story)


# 使用该函数
generate_pdf("./", "output_code.pdf", ".pdfignore.yml")
