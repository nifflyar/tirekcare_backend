from sqlalchemy.ext.asyncio import AsyncSession

from src.models.video import VideoOrm
from src.repositories.base_repository import BaseRepository



class VideoRepository(BaseRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(db=db, model=VideoOrm)

    
