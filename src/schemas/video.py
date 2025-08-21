from pydantic import BaseModel
from typing import Optional



class VideoCreateSchema(BaseModel):
    title: str
    description: str
    url: str



class VideoUpdateSchema(BaseModel):
    title: str
    description: str
    url: str


class VideoEditSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None


class VideoResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    url: str


class VideoInDBSchema(VideoCreateSchema):

    model_config = {
        "from_attributes": True
    }



