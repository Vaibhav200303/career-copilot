from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
from app.crud import get_user_by_email
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.db import get_db

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(
        plain_password:str,
        hashed_password:str
)->bool:
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data:dict)->str:
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def authenticate_user(db:Session,email:str,password:str):
    user=get_user_by_email(db,email)
    if not user:
        return None
    if not verify_password(password,user.hashed_password):
        return None
    return user
    
def decode_access_token(token:str)->dict:
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    try:
        payload=decode_access_token(token)
        email=payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401,detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")
    user=get_user_by_email(db,email)
    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    return user
