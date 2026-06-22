from datetime import datetime
from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship
from app.db import Base

class Document(Base):
    __tablename__="documents"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False,index=True)
    source_type=Column(String,nullable=False)
    source_id=Column(Integer,nullable=False)
    content=Column(Text,nullable=False)
    embedding=Column(Vector[768],nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow,nullable=False)

    user = relationship(
        "User",
        back_populates="documents"
    )