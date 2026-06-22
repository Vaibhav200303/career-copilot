from pydantic import BaseModel, ConfigDict


class JobDescriptionCreate(BaseModel):
    title: str
    content: str


class JobDescriptionResponse(BaseModel):
    id: int
    title: str
    content: str

    model_config = ConfigDict(
        from_attributes=True
    )