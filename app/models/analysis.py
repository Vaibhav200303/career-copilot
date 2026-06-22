from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.db import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False,
        index=True,
    )

    job_description_id = Column(
        Integer,
        ForeignKey("job_descriptions.id"),
        nullable=False,
        index=True,
    )

    matched_skills = Column(
        JSONB,
        nullable=False,
    )

    missing_skills = Column(
        JSONB,
        nullable=False,
    )

    recommendations = Column(
        JSONB,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="analyses",
    )

    resume = relationship(
        "Resume",
        back_populates="analyses",
    )

    job_description = relationship(
        "JobDescription",
        back_populates="analyses",
    )

    roadmaps = relationship(
        "Roadmap",
        back_populates="analysis",
        cascade="all, delete-orphan",
    )

    interviews = relationship(
        "Interview",
        back_populates="analysis",
        cascade="all, delete-orphan",
    )