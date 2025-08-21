from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.video import VideoCreateSchema, VideoInDBSchema
from src.repositories.video_repository import VideoRepository



class VideoService:
    def __init__(self, db: AsyncSession):
        self.video_repo = VideoRepository(db)


    async def _get_or_404(self, video_id: int):
        video_obj = await self.video_repo.get_by_id(video_id)
        if not video_obj:
            raise HTTPException(status_code=404, detail="The Video is not found")
        return video_obj

    
    async def add_video(self, video_data: VideoCreateSchema) -> None:
        video_create = VideoInDBSchema.model_validate(video_data)
        await self.video_repo.create(video_create)

    

    async def get_video(self):
        return await self.video_repo.get_all()


    async def get_video_by_id(self, video_id: int):
        video_obj = await self._get_or_404(video_id)
        return video_obj

    async def update_video(self, video_id: int, video_data) -> None:
        if await self._get_or_404(video_id):
            await self.video_repo.update_by_id(video_id, video_data)


    async def delete_video(self, video_id) -> None:
        if await self._get_or_404(video_id):
            await self.video_repo.delete_by_id(video_id)

