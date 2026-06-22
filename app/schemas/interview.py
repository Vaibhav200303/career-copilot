from pydantic import BaseModel


class InterviewQuestion(BaseModel):
    question: str
    category: str
    difficulty: str


class InterviewResponse(BaseModel):
    questions: list[InterviewQuestion]