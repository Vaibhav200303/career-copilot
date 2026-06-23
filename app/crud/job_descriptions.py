from sqlalchemy.orm import Session

from app.models import JobDescription
from app.schemas import JobDescriptionCreate


def create_job_description(
    db: Session,
    user_id: int,
    job: JobDescriptionCreate
):
    job_description = JobDescription(
        user_id=user_id,
        **job.model_dump()
    )

    db.add(job_description)
    db.commit()
    db.refresh(job_description)

    return job_description


def get_job_description_by_id(
    job_id: int,
    db: Session
):
    return (
        db.query(JobDescription)
        .filter(JobDescription.id == job_id)
        .first()
    )


def get_job_descriptions_by_user(
    db: Session,
    user_id: int,
):
    return (
        db.query(JobDescription)
        .filter(
            JobDescription.user_id == user_id
        )
        .all()
    )