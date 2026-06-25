from app.db import Base
from sqlalchemy import Column,String,Integer,ForeignKey,Text,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
class ChatMessage(Base):
    __tablename__="chat_messages"
    id=Column(Integer,primary_key=True,index=True)
    conversation_id=Column(Integer,ForeignKey("conversations.id"),nullable=False,index=True)
    role=Column(String,nullable=False)
    content=Column(Text,nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)
    conversation=relationship("Conversation",back_populates="chat_messages")