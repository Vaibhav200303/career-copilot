from fastapi import FastAPI,Depends
from app.db import engine
from sqlalchemy import text
from app.schemas import UserResponse,UserCreate
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import create_user


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
    return create_user(db,user)