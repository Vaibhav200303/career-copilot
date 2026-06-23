from sqlalchemy.orm import Session

from app.models import Analysis


def create_analysis(
    db: Session,
    user_id: int,
    resume_id: int,
    job_description_id: int,
    analysis: dict
):
    db_analysis = Analysis(
        user_id=user_id,
        resume_id=resume_id,
        job_description_id=job_description_id,
        matched_skills=analysis["matched_skills"],
        missing_skills=analysis["missing_skills"],
        recommendations=analysis["recommendations"]
    )

    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return db_analysis


def get_analysis_by_id(
    db: Session,
    analysis_id: int
):
    return (
        db.query(Analysis)
        .filter(Analysis.id == analysis_id)
        .first()
    )

def get_analyses_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(Analysis)
        .filter(
            Analysis.user_id == user_id
        )
        .all()
    )