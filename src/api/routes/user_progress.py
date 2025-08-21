from fastapi import APIRouter


from src.schemas.user_progress import UserProgressEditSchema, UserProgressResponseSchema, UserProgressUpdateSchema, UserProgressCreateSchema
from src.services.user_progress_service import UserProgressService
from src.db.dependencies import DbSessionDep




router = APIRouter(prefix="/user_progress", tags=["User Progress"])



@router.post("")
async def add_user_progress(db: DbSessionDep, progress_data: UserProgressCreateSchema):
    user_progress_service = UserProgressService(db)
    await user_progress_service.add_user_progress(progress_data)
    return {"msg": "The User Progress has been added"}



@router.get("", response_model=list[UserProgressResponseSchema])
async def get_user_progresses(db: DbSessionDep):
    user_progress_service = UserProgressService(db)
    return await user_progress_service.get_user_progress()



@router.get("/by-id/{user_progress_id}", response_model=UserProgressResponseSchema)
async def get_user_progress(db: DbSessionDep, user_progress_id: int):
    user_progress_service = UserProgressService(db)
    return await user_progress_service.get_user_progress_by_id(user_progress_id)

@router.get("/by-user/{user_id}", response_model=list[UserProgressResponseSchema])
async def get_user_progress_by_user_id(db: DbSessionDep, user_id: int):
    user_progress_service = UserProgressService(db)
    return await user_progress_service.get_user_progress_by_user_id(user_id)



@router.patch("/{user_progress_id}")
async def edit_user_progress(db: DbSessionDep, user_progress_id: int, progress_data: UserProgressEditSchema):
    user_progress_service = UserProgressService(db)
    await user_progress_service.update_user_progress(user_progress_id, progress_data)
    return {"msg": "User Progress has been edited"}


@router.put("/{user_progress_id}")
async def update_user_progress(db: DbSessionDep, user_progress_id: int, progress_data: UserProgressUpdateSchema):
    user_progress_service = UserProgressService(db)
    await user_progress_service.update_user_progress(user_progress_id, progress_data)
    return {"msg": "User Progress has been updated"}


@router.delete("/{user_progress_id}")
async def delete_user_progress(db: DbSessionDep, user_progress_id: int):
    user_progress_service = UserProgressService(db)
    await user_progress_service.delete_user_progress(user_progress_id)
    return {"msg": "User Progress has been deleted"}



@router.get("/count/{user_id}")
async def count_user_progress_by_user_id(db: DbSessionDep, user_id: int):
    user_progress_service = UserProgressService(db)
    return await user_progress_service.count_user_progress(user_id)
