from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User
from fastapi import HTTPException

def create_user(db:Session,user:UserCreate):
    existing=db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=409,detail="Email already registered")
    db_user=User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user