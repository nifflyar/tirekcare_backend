import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional





class TaskCreateSchema(BaseModel):
    title: str
    description: str
    max_points: int
    



class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    max_points: int


class TaskEditSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    max_points: Optional[int] = None

class TaskUpdateSchema(TaskCreateSchema):
    pass



class TaskInDBSchema(BaseModel):
    title: str
    description: str
    max_points: int

    model_config = {
        "from_attributes": True
    }



