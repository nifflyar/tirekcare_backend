from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from src.schemas.user_progress import UserProgressCreateSchema, UserProgressInDBSchema
from src.repositories.user_progress_repository import UserProgressRepository




class UserProgressService:
    def __init__(self, db: AsyncSession):
        self.user_progress_repo = UserProgressRepository(db)

    

    async def _get_or_404(self, progress_id: int):
        progress_obj = await self.user_progress_repo.get_by_id(progress_id)
        if progress_obj is None:
            raise HTTPException(status_code=404, detail="The User Progress is not found")
        return progress_obj

    
    async def add_user_progress(self, progress_data: UserProgressCreateSchema) -> None:
        progress_create = UserProgressInDBSchema.model_validate(progress_data)

        user_obj = await self.user_progress_repo.get_user_by_id(progress_data.user_id)
        task_obj = await self.user_progress_repo.get_task_by_id(progress_data.task_id)
        if not user_obj and not task_obj:
            raise HTTPException(status_code=404, detail="User or Task is not found")
            
        progress_obj = await self.user_progress_repo.get_progress_by_taskid_userid(progress_data.user_id, progress_data.task_id)
        if progress_obj:
            raise HTTPException(status_code=400, detail="That UserProgress already exists")
        
        await self.user_progress_repo.create(progress_create)
        
    

    async def get_user_progress(self):
        return await self.user_progress_repo.get_user_progress()


    async def get_user_progress_by_id(self, progress_id: int):
        progress_obj = await self.user_progress_repo.get_user_progress_by_id(progress_id)
        if progress_obj is None:
            raise HTTPException(status_code=404, detail="The User Progress is not found")
        return progress_obj
    
    async def get_user_progress_by_user_id(self, user_id: int):
        user_obj = await self.user_progress_repo.get_user_by_id(user_id)
        if user_obj is None:
            raise HTTPException(status_code=404, detail="The User is not found")
        progress_obj = await self.user_progress_repo.get_user_progress_by_user_id(user_id)
        return progress_obj
    

    async def update_user_progress(self, progress_id: int, progress_data) -> None:
        if await self._get_or_404(progress_id):
            await self.user_progress_repo.update_by_id(progress_id, progress_data)


    async def delete_user_progress(self, progress_id) -> None:
        if await self._get_or_404(progress_id):
            await self.user_progress_repo.delete_by_id(progress_id)


    async def count_user_progress(self, user_id: int):
        progress_count = await self.user_progress_repo.count_user_progress_by_user_id(user_id)
        if not progress_count:
            raise HTTPException(status_code=404, detail="The User is not found")
        return progress_count



