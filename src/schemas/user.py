import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional





class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    

class UserLoginSchema(UserCreateSchema):
    pass


class UserResponseSchema(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime.datetime
    updated_at: datetime.datetime



class UserEditSchema(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None

class UserUpdateSchema(UserCreateSchema):
    role : str



class UserInDBSchema(BaseModel):
    email: EmailStr
    hashed_password: str
    role: str

    model_config = {
        "from_attributes": True
    }



