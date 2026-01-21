from fastapi import APIRouter, UploadFile, File
from src.tools.pdf_tool import extract_pdf_text

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_pdf_text(file.file)
    return {
        "message": "PDF processed successfully",
        "text_preview": text[:500]
    }
