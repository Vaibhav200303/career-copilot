from app.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from datetime import datetime

class Conversation(Base):
    __tablename__="conversations"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False,index=True)
    title=Column(String(100),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)
    last_message_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    user=relationship("User",back_populates="conversations")
    chat_messages=relationship("ChatMessage",back_populates="conversation",cascade="all,delete-orphan")