from sqlalchemy.orm import Session
from app.schemas import JobDescriptionCreate
from app.models import User,Resume,JobDescription
from fastapi import HTTPException
from pydantic import EmailStr


def get_user_by_email(db:Session,email:EmailStr):
    return db.query(User).filter(User.email==email).first()


def create_user(db:Session,user:dict):
    existing=db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=409,detail="Email already registered")
    
    db_user=User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_resume(
        db:Session,
        user_id:int,
        file_name:str,
        file_path:str,
        extracted_text:str
):
    resume=Resume(user_id=user_id,file_name=file_name,file_path=file_path,extracted_text=extracted_text)
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


def create_job_description(
        db:Session,
        user_id:int,
        job:JobDescriptionCreate
):
    job_description=JobDescription(
        user_id=user_id,
        **job.model_dump()
    )
    db.add(job_description)
    db.commit()
    db.refresh(job_description)
    return job_description


def get_resume_by_id(
        resume_id:int,
        db:Session
):
    resume=db.query(Resume).filter(Resume.id==resume_id).first()
    return resume

def get_job_description_by_id(
        job_id:int,
        db:Session
):
    job=db.query(JobDescription).filter(JobDescription.id==job_id).first()
    return job
