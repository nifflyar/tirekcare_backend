
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import async_session


async def get_db_session():
    async with async_session() as session:
        yield session



DbSessionDep = Annotated[AsyncSession, Depends(get_db_session)]