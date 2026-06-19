from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User
from fastapi import HTTPException
from app.auth import hash_password

def create_user(db:Session,user:UserCreate):
    existing=db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=409,detail="Email already registered")
    user_data=user.model_dump()
    user_data["hashed_password"]=hash_password(user_data.pop("password"))
    db_user=User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user