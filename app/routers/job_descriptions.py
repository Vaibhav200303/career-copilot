from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.document_ingestion import ingest_document
from app.core import get_current_user
from app.crud import create_job_description
from app.db import get_db
from app.models import User
from app.schemas import (
    JobDescriptionCreate,
    JobDescriptionResponse,
)

router = APIRouter(
    prefix="/job-description",
    tags=["Job Descriptions"],
)


@router.post(
    "",
    response_model=JobDescriptionResponse,
    status_code=201,
)
def create_job(
    job: JobDescriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    job_description = create_job_description(
        db=db,
        user_id=current_user.id,
        job=job,
    )
    ingest_document(
        db=db,
        user_id=current_user.id,
        source_type="job_description",
        source_id=job_description.id,
        content=job_description.content,
    )
    return job_description