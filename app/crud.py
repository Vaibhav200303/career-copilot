from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User
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