
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import UserOrm
from src.repositories.base_repository import BaseRepository



class UserRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=UserOrm)
    
    
    async def get_user_by_email(self, email: str) -> UserOrm | None:
        """Returns a user based on the given email"""
        stmt = select(UserOrm).filter(UserOrm.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()