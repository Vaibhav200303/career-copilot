from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core import get_current_user
from app.crud import (
    create_interview,
    get_analysis_by_id,
)
from app.db import get_db
from app.models import User
from app.schemas import InterviewResponse
from app.services.interview import generate_interview_questions

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"],
)


@router.post(
    "/{analysis_id}",
    response_model=InterviewResponse,
    status_code=201,
)
def generate_interview(
    analysis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    analysis = get_analysis_by_id(
        db,
        analysis_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found",
        )

    if analysis.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    interview = generate_interview_questions(
        matched_skills=analysis.matched_skills,
        missing_skills=analysis.missing_skills,
    )

    create_interview(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis.id,
        content=interview.model_dump(),
    )

    return interview