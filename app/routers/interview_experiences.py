from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.core import get_current_user
from app.db import get_db

from app.models import User

from app.schemas import (
    InterviewExperienceCreate,
    InterviewExperienceUpdate,
    InterviewExperienceResponse,
)

from app.crud.interview_experiences import (
    get_interview_experience_by_id,
    get_interview_experiences_by_user,
)

from app.services.interview_experiences import (
    create_interview_experience_service,
    update_interview_experience_service,
    delete_interview_experience_service,
)


router = APIRouter(
    prefix="/interview-experiences",
    tags=["Interview Experiences"],
)


@router.post(
    "",
    response_model=InterviewExperienceResponse,
    status_code=201,
)
def create_interview_experience(
    interview: InterviewExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_interview_experience_service(
        db=db,
        user_id=current_user.id,
        interview_data=interview,
    )

@router.get(
    "",
    response_model=list[InterviewExperienceResponse],
)
def get_interview_experiences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_interview_experiences_by_user(
        db=db,
        user_id=current_user.id,
    )



@router.get(
    "/{interview_id}",
    response_model=InterviewExperienceResponse,
)
def get_interview_experience(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    interview = get_interview_experience_by_id(
        db=db,
        interview_id=interview_id,
    )

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found",
        )

    if interview.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    return interview



@router.put(
    "/{interview_id}",
    response_model=InterviewExperienceResponse,
)
def update_interview_experience(
    interview_id: int,
    interview_data: InterviewExperienceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    interview = get_interview_experience_by_id(
        db=db,
        interview_id=interview_id,
    )

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found",
        )

    if interview.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    return update_interview_experience_service(
        db=db,
        interview=interview,
        update_data=interview_data.model_dump(
            exclude_unset=True
        ),
    )

@router.delete(
    "/{interview_id}",
)
def delete_interview_experience(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    interview = get_interview_experience_by_id(
        db=db,
        interview_id=interview_id,
    )

    if not interview:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found",
        )

    if interview.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied",
        )

    delete_interview_experience_service(
        db=db,
        interview=interview,
    )

    return {
        "message": "Interview experience deleted successfully"
    }