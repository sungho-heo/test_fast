import os
from app.parsers.markitdown_parser import read_markitdown
from pdf_parser import read_pdf
from docx_parser import read_docx

def read_file(path:str):
    
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        return read_pdf(path)
    
    if ext == ".docx":
        return read_docx(path)
    
    # 나머지 확장자는 다 이걸로
    return read_markitdown(path)