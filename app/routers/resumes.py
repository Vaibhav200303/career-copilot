import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core import get_current_user
from app.crud import create_resume
from app.db import get_db
from app.models import User
from app.services.pdf import extract_text_from_pdf

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)

UPLOAD_DIR = Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("")
async def upload_resume(
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed",
        )

    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = UPLOAD_DIR / unique_filename

    contents = await file.read()

    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    extracted_text = extract_text_from_pdf(str(file_path))

    resume = create_resume(
        db,
        current_user.id,
        unique_filename,
        str(file_path),
        extracted_text,
    )

    return {
        "id": resume.id,
        "filename": resume.file_name,
    }