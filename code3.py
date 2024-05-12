import os
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

def load_exclusions(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    excluded_dirs = set(config.get('directories', []))
    excluded_files = set(config.get('files', []))
    return excluded_dirs, excluded_files

def generate_pdf(source_folder, output_pdf, config_path):
    excluded_dirs, excluded_files = load_exclusions(config_path)
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='STSong-Light', fontSize=10, leading=12)

    for root, dirs, files in os.walk(source_folder, topdown=True):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]  # Modify the dirs in-place to skip excluded directories
        for filename in files:
            if any(filename.endswith(ext) for ext in ['.py', '.txt']):  # Extend or change file types as needed
                if filename not in excluded_files and not any(root.startswith(os.path.join(source_folder, d)) for d in excluded_dirs):
                    filepath = os.path.join(root, filename)
                    with open(filepath, 'r', encoding='utf-8') as file:
                        code = file.read()
                        story.append(Paragraph(f"File: {filename}", styles['Title']))
                        for line in code.splitlines():
                            story.append(Paragraph(line.replace(' ', '&nbsp;'), code_style))
                        story.append(Spacer(1, 12))
    
    doc.build(story)

# 使用该函数
generate_pdf('./', 'output_code3.pdf', '.pdfignore.yml')
