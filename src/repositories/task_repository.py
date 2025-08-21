from sqlalchemy.ext.asyncio import AsyncSession

from src.models.task import TaskOrm
from src.repositories.base_repository import BaseRepository




class TaskRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=TaskOrm)

    

    
