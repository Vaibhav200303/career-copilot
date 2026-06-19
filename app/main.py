from fastapi import FastAPI,Depends, HTTPException
from app.db import engine
from sqlalchemy import text
from app.schemas import UserResponse,UserCreate,Token,UserLogin
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import create_user
from app.auth import authenticate_user,create_access_token
from app.auth import hash_password

app=FastAPI(title="Career Copilot")

@app.get("/")
def health_check():
    return {"message":"working"}

@app.get("/db-check")
def db_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "connection healthy"}

@app.post("/users",response_model=UserResponse,status_code=201)
def create_new_user(user:UserCreate,db:Session=Depends(get_db)):
    user_data=user.model_dump()
    user_data["hashed_password"]=hash_password(user_data.pop("password"))
    return create_user(db,user_data)


@app.post("/login",response_model=Token)
def login(user_credential:UserLogin,db:Session=Depends(get_db)):
    user=authenticate_user(db,user_credential.email,user_credential.password)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    access_token=create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}

