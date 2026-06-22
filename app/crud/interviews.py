from sqlalchemy.orm import Session

from app.models import Interview


def create_interview(
    db: Session,
    user_id: int,
    analysis_id: int,
    content: dict
):
    interview = Interview(
        user_id=user_id,
        analysis_id=analysis_id,
        content=content
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview