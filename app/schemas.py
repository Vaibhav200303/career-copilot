from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr

    model_config=ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email:EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str

class JobDescriptionCreate(BaseModel):
    title:str
    content:str
class JobDescriptionResponse(BaseModel):
    id:int
    title:str
    content:str
    model_config=ConfigDict(from_attributes=True)

class SkillGapResponse(BaseModel):
    matched_skills:list[str]
    missing_skills:list[str]
    recommendations:list[str]

class AnalysisResponse(BaseModel):
    id: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommendations: list[str]

    model_config = ConfigDict(
        from_attributes=True
    )



class RoadmapWeek(BaseModel):
    week: int
    topics: list[str]
    project: str
    outcome: str


class RoadmapResponse(BaseModel):
    weeks: list[RoadmapWeek]