from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User,Resume
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
        file_path:str
):
    resume=Resume(user_id=user_id,file_name=file_name,file_path=file_path)
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume