import fitz
from PIL import Image
import pytesseract
import io
import os

pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")
# Pdf file read
def read_pdf(path:str):
    
    doc = fitz.open(path)
    
    text =""
    
    for page in doc:
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))

        text += pytesseract.image_to_string(img, lang="kor+eng")

    return text.strip()