from fastapi import APIRouter

from src.api.routes.database import router as database_router
from src.api.routes.auth import router as auth_router
from src.api.routes.video import router as video_router
from src.api.routes.user import router as user_router
from src.api.routes.task import router as task_router
from src.api.routes.user_progress import router as user_progress_router
from src.api.routes.payment import router as payment_router

main_router = APIRouter()#prefix="/api/v1")

routers = [database_router, payment_router, auth_router, user_router, 
           task_router, user_progress_router, video_router]

for router in routers:
    main_router.include_router(router)