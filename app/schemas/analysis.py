from pydantic import BaseModel, ConfigDict


class SkillGapResponse(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    recommendations: list[str]


class AnalysisResponse(BaseModel):
    id: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommendations: list[str]

    model_config = ConfigDict(
        from_attributes=True
    )