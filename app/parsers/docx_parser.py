from docx import Document

def read_docx(path:str):
    
    doc = Document(path)
    
    text =""
    
    for para in doc.paragraphs:
        text += para.text + "\n"
    
    # 띄워쓰기같은거 없애줌.
    return text.strip()