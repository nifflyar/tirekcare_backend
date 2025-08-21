from typing import override
from sqlalchemy import select, func, and_
from sqlalchemy.orm import aliased
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.task import TaskOrm
from src.models.user import UserOrm, UserProgressOrm
from src.repositories.base_repository import BaseRepository



class UserProgressRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=UserProgressOrm)
    
    async def get_user_progress_by_user_id(self, user_id: int) -> UserProgressOrm | None:
        """Returns a user progress based on the given user_id"""
        stmt = (select(UserProgressOrm).filter(UserProgressOrm.user_id == user_id))
        result = await self.db.execute(stmt)
        return result.scalars()
    
    async def get_user_progress(self):
        stmt = select(UserProgressOrm)
        result = await self.db.execute(stmt)
        return result.scalars()


    async def get_user_progress_by_id(self, progress_id: int):
        stmt = select(UserProgressOrm).filter(UserProgressOrm.id == progress_id)
        result = await self.db.execute(stmt)
        return result.scalar()
    

    async def count_user_progress_by_user_id(self, user_id: int):
        stmt = (select(func.count())
                .where(UserProgressOrm.user_id == user_id))
        result = await self.db.execute(stmt)
        return {"progress_count": result.scalar()}
    
    async def get_task_by_id(self, task_id: int):
        stmt = select(TaskOrm).where(TaskOrm.id == task_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
    
    async def get_progress_by_taskid_userid(self, user_id: int, task_id: int):
        stmt = select(UserProgressOrm).filter(and_(
            UserProgressOrm.user_id == user_id,
            UserProgressOrm.task_id == task_id))
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    @override
    async def get_user_by_id(self, user_id: int):
        stmt = select(UserOrm).where(UserOrm.id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()