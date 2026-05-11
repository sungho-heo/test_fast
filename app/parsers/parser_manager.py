import os
from app.parsers.txt_parser import read_txt
from app.parsers.pdf_parser import read_pdf

def read_file(path:str):
    
    ext = os.path.splitext(path)[1].lower()
    
    if ext == ".txt":
        return read_txt(path)

    if ext == ".pdf":
        return read_pdf(path)
    
    return ValueError("지원하지 않는 파일 형식입니다.")