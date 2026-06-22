from app.db import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey, Text
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True,nullable=False)
    hashed_password=Column(String,nullable=False)
    
    resumes = relationship(
        "Resume",
        back_populates="user"
    )
    job_descriptions = relationship(
        "JobDescription",
        back_populates="user"
    )

class Resume(Base):
    __tablename__="resumes"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    file_name=Column(String,nullable=False)
    file_path=Column(String,nullable=False,unique=True)
    uploaded_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    extracted_text=Column(Text,nullable=True)
    user = relationship(
        "User",
        back_populates="resumes"
    )

class JobDescription(Base):
    __tablename__="job_description"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    title=Column(String,nullable=False)
    content=Column(Text,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    user=relationship("User",back_populates="job_descriptions")