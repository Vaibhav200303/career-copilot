from pydantic import BaseModel


class RoadmapWeek(BaseModel):
    week: int
    topics: list[str]
    project: str
    outcome: str


class RoadmapResponse(BaseModel):
    weeks: list[RoadmapWeek]