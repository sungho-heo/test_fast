import fitz

# Pdf file read
def read_pdf(path:str):
    
    doc = fitz.open(path)
    
    text =""
    
    for page in doc:
        if type(page) ==str:
            text = text + page.get_text()
    return text