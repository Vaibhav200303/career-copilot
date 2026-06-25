from datetime import date, datetime

from pydantic import BaseModel


class InterviewExperienceCreate(BaseModel):
    company: str
    role: str
    interview_type: str
    interview_date: date
    outcome: str
    questions_asked: list[str]
    experience: str
    lessons_learned: str


class InterviewExperienceUpdate(BaseModel):
    company: str | None = None
    role: str | None = None
    interview_type: str | None = None
    interview_date: date | None = None
    outcome: str | None = None
    questions_asked: list[str] | None = None
    experience: str | None = None
    lessons_learned: str | None = None

class InterviewExperienceResponse(BaseModel):
    id: int

    company: str
    role: str

    interview_type: str
    interview_date: date

    outcome: str

    questions_asked: list[str]

    experience: str
    lessons_learned: str

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }