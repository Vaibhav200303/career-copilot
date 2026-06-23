from app.db import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Text
from datetime import datetime
from sqlalchemy.orm import relationship

class Note(Base):
    __tablename__="notes"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),index=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(Text,nullable=False)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    user=relationship("User",back_populates="notes")

