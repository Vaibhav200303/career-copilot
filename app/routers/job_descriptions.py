from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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
    return create_job_description(
        db=db,
        user_id=current_user.id,
        job=job,
    )