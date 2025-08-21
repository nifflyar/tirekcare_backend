from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from src.repositories.task_repository import TaskRepository
from src.schemas.task import TaskCreateSchema, TaskInDBSchema



class TaskService:
    def __init__(self, db: AsyncSession):
        self.task_repo = TaskRepository(db)

    

    async def _get_or_404(self, task_id: int):
        task_obj = await self.task_repo.get_by_id(task_id)
        if not task_obj:
            raise HTTPException(status_code=404, detail="The Task is not found")
        return task_obj

    
    async def add_task(self, task_data: TaskCreateSchema) -> None:
        task_create = TaskInDBSchema.model_validate(task_data)
        await self.task_repo.create(task_create)

    

    async def get_task(self):
        return await self.task_repo.get_all()


    async def get_task_by_id(self, task_id: int):
        task_obj = await self._get_or_404(task_id)
        return task_obj

    async def update_task(self, task_id: int, task_data) -> None:
        if await self._get_or_404(task_id):
            await self.task_repo.update_by_id(task_id, task_data)


    async def delete_task(self, task_id) -> None:
        if await self._get_or_404(task_id):
            await self.task_repo.delete_by_id(task_id)



