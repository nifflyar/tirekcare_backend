from fastapi import APIRouter


from src.schemas.user import UserEditSchema, UserResponseSchema, UserUpdateSchema
from src.services.user_service import UserService
from src.db.dependencies import DbSessionDep




router = APIRouter(prefix="/user", tags=["User"])




@router.get("", description="w/o password", response_model=list[UserResponseSchema])
async def get_users(db: DbSessionDep):
    user_service = UserService(db)
    return await user_service.get_user()



@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user(db: DbSessionDep, user_id: int):
    user_service = UserService(db)
    return await user_service.get_user_by_id(user_id)



@router.patch("/{user_id}")
async def edit_user(db: DbSessionDep, user_id: int, user_data: UserEditSchema):
    user_service = UserService(db)
    await user_service.update_user(user_id, user_data)
    return {"msg": "User has been edited"}


@router.put("/{user_id}")
async def update_user(db: DbSessionDep, user_id: int, user_data: UserUpdateSchema):
    user_service = UserService(db)
    await user_service.update_user(user_id, user_data)
    return {"msg": "User has been updated"}


@router.delete("/{user_id}")
async def delete_user(db: DbSessionDep, user_id: int):
    user_service = UserService(db)
    await user_service.delete_user(user_id)
    return {"msg": "User has been deleted"}

