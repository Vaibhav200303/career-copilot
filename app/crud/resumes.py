from sqlalchemy.orm import Session

from app.models import Resume


def create_resume(
    db: Session,
    user_id: int,
    file_name: str,
    file_path: str,
    extracted_text: str
):
    resume = Resume(
        user_id=user_id,
        file_name=file_name,
        file_path=file_path,
        extracted_text=extracted_text
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_resume_by_id(
    resume_id: int,
    db: Session
):
    return (
        db.query(Resume)
        .filter(Resume.id == resume_id)
        .first()
    )

def get_resumes_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(Resume)
        .filter(
            Resume.user_id == user_id
        )
        .all()
    )