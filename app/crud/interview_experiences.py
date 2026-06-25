from sqlalchemy.orm import Session
from app.models import InterviewExperience
def create_interview_experience(
    db: Session,
    user_id: int,
    company: str,
    role: str,
    interview_type: str,
    interview_date,
    outcome: str,
    questions_asked: list[str],
    experience: str,
    lessons_learned: str,
):
    interview = InterviewExperience(
        user_id=user_id,
        company=company,
        role=role,
        interview_type=interview_type,
        interview_date=interview_date,
        outcome=outcome,
        questions_asked=questions_asked,
        experience=experience,
        lessons_learned=lessons_learned,
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview

def get_interview_experience_by_id(
    db: Session,
    interview_id: int,
):
    return (
        db.query(InterviewExperience)
        .filter(
            InterviewExperience.id == interview_id
        )
        .first()
    )




def get_interview_experiences_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(InterviewExperience)
        .filter(
            InterviewExperience.user_id == user_id
        )
        .order_by(
            InterviewExperience.interview_date.desc()
        )
        .all()
    )


def update_interview_experience(
    db: Session,
    interview: InterviewExperience,
    update_data: dict,
):
    for field, value in update_data.items():
        setattr(
            interview,
            field,
            value,
        )

    db.commit()
    db.refresh(interview)

    return interview



def delete_interview_experience(
    db: Session,
    interview: InterviewExperience,
):
    db.delete(interview)
    db.commit()