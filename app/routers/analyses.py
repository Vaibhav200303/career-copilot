from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core import get_current_user
from app.crud import (
    create_analysis,
    get_job_description_by_id,
    get_resume_by_id,
)
from app.db import get_db
from app.models import User
from app.schemas import AnalysisResponse
from app.services.ai import analyze_skill_gap

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.post(
    "/{resume_id}/{job_id}",
    response_model=AnalysisResponse,
    status_code=201,
)
def analyze_resume(
    resume_id: int,
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    resume = get_resume_by_id(resume_id, db)
    job = get_job_description_by_id(job_id, db)

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job description not found",
        )

    if resume.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    if job.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    analysis = analyze_skill_gap(
        resume_text=resume.extracted_text,
        job_description=job.content,
    )

    db_analysis = create_analysis(
        db=db,
        user_id=current_user.id,
        resume_id=resume.id,
        job_description_id=job.id,
        analysis=analysis,
    )

    return db_analysis