from fastapi import FastAPI, UploadFile, File
import os
from utils.file_reader import read_txt
from core.ollama_client import summarize
from db.base import Base
# from db.session import engine
# from models.document import Document


app = FastAPI()

UPLOAD_DIR = "storage/uploads"
#데이터베이스 모델정의
# Document
# --------
# id (UUID) int
# filename string
# stored_path string 실제파일경로
# file_type string 파일 확장자.
# created_at Date 문서 업로드일 = 요약일 
# status (uploaded / parsed / summarized) Enum(열거형) 특정값만 들어갈수있음. 이건 작업단계 프론트에 보내기위함.

# Summary
# --------
# id int
# document_id (FK) int
# summary_text string 문서 요약 텍스트.
# created_at Date 문서 요약일

# 추가할에정인거 문서가 업로드되는 개당 root/file/upload/문서_id값
@app.post("/upload")
async def upload(file: UploadFile= File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

# wb 바이너리 파일 읽기 pdf,한글, 워드문서.
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    return {
        "filename": file.filename,
        "stored_path": file_path
    }
# #POST 처리할 문서 받기
@app.post("/summarize")
# 업로드할 파일
async def summarize_file(filename: str):
    path= f"storage/uploads/{filename}"
    
    text = read_txt(path)
    result = summarize(text)
    
    return {
        "summary": result
    }


