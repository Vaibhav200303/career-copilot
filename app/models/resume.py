from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    file_name = Column(String, nullable=False)

    file_path = Column(
        String,
        nullable=False,
        unique=True,
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    extracted_text = Column(
        Text,
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="resumes",
    )

    analyses = relationship(
        "Analysis",
        back_populates="resume",
        cascade="all, delete-orphan",
    )