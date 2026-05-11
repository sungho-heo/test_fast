import fitz
from PIL import Image
import pytesseract
import io

# Pdf file read
def read_pdf(path:str):
    
    doc = fitz.open(path)
    
    text =""
    
    for page in doc:
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))

        text += pytesseract.image_to_string(img, lang="kor+eng")

    return text.strip()