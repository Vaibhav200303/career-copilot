from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    resumes = relationship(
        "Resume",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    job_descriptions = relationship(
        "JobDescription",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    roadmaps = relationship(
        "Roadmap",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    analyses = relationship(
        "Analysis",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    roadmaps = relationship(
        "Roadmap",
        back_populates="user"
    )


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


class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    title = Column(String, nullable=False)

    content = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="job_descriptions",
    )

    analyses = relationship(
        "Analysis",
        back_populates="job_description",
        cascade="all, delete-orphan",
    )



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
        back_populates="analysis"
    )




class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    analysis_id = Column(
        Integer,
        ForeignKey("analyses.id"),
        nullable=False
    )

    content = Column(JSONB, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="roadmaps"
    )

    analysis = relationship(
        "Analysis",
        back_populates="roadmaps"
    )