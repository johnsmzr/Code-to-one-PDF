import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf(source_folder, output_pdf):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', fontSize=10, leading=12)

    for filename in sorted(os.listdir(source_folder)):
        if filename.endswith(".py"):  # 根据需要调整文件类型
            filepath = os.path.join(source_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                code = file.read()
                story.append(Paragraph(f"File: {filename}", styles['Title']))
                for line in code.splitlines():
                    story.append(Paragraph(line.replace(' ', '&nbsp;'), code_style))
                story.append(Spacer(1, 12))
    
    doc.build(story)

# 使用该函数
generate_pdf('./', 'output_code2.pdf')
