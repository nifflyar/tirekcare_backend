from pydantic import BaseModel
from typing import Optional






class UserProgressCreateSchema(BaseModel):
    task_id: int
    user_id: int
    user_points: int


class UserProgressUpdateSchema(BaseModel):
    task_id: int
    user_id: int
    user_points: int


class UserProgressEditSchema(BaseModel):
    task_id: Optional[int] = None
    user_id: Optional[int] = None
    user_points: Optional[int] = None


class UserProgressResponseSchema(BaseModel):
    id: int
    task_id: int
    user_id: int
    user_points: int

    model_config = {
        "from_attributes": True
    }



class UserProgressInDBSchema(UserProgressCreateSchema):

    model_config = {
        "from_attributes": True
    }