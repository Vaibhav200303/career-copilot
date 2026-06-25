from datetime import date, datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.db import Base


class InterviewExperience(Base):
    __tablename__ = "interview_experiences"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    company = Column(
        String,
        nullable=False,
    )

    role = Column(
        String,
        nullable=False,
    )

    interview_type = Column(
        String,
        nullable=False,
    )

    interview_date = Column(
        Date,
        nullable=False,
    )

    outcome = Column(
        String,
        nullable=False,
    )

    questions_asked = Column(
        JSONB,
        nullable=False,
    )

    experience = Column(
        Text,
        nullable=False,
    )

    lessons_learned = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="interview_experiences",
    )