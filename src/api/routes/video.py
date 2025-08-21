from fastapi import APIRouter

from src.services.video_service import VideoService
from src.db.dependencies import DbSessionDep
from src.schemas.video import VideoEditSchema, VideoResponseSchema, VideoCreateSchema, VideoUpdateSchema


router = APIRouter(prefix="/videos", tags=["Video"])





@router.post("")
async def add_videos(db: DbSessionDep, video_data: VideoCreateSchema):
    video_service = VideoService(db)
    await video_service.add_video(video_data)
    return {"msg": "The video has been added"}


@router.get("", response_model=list[VideoResponseSchema])
async def get_videos(db: DbSessionDep):
    video_service = VideoService(db)
    return await video_service.get_video()


@router.get("/{video_id}", response_model=VideoResponseSchema)
async def get_video(db: DbSessionDep, video_id: int):
    video_service = VideoService(db)
    return await video_service.get_video_by_id(video_id)



@router.patch("/{video_id}")
async def edit_video(db: DbSessionDep, video_id: int, video_data: VideoEditSchema):
    video_service = VideoService(db)
    await video_service.update_video(video_id, video_data)
    return {"msg": "Video has been edited"}


@router.put("/{video_id}")
async def update_video(db: DbSessionDep, video_id: int, video_data: VideoUpdateSchema):
    video_service = VideoService(db)
    await video_service.update_video(video_id, video_data)
    return {"msg": "Video has been updated"}


@router.delete("/{video_id}")
async def delete_video(db: DbSessionDep, video_id: int):
    video_service = VideoService(db)
    await video_service.delete_video(video_id)
    return {"msg": "Video has been deleted"}

