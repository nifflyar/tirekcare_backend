from fastapi import APIRouter

from src.services.db_service import drop_create_db



router = APIRouter(prefix="/db", tags=["System"])



@router.post("/drop_create_DB", description="Drop and Create DB")
async def setup_database():
    await drop_create_db()
    return {"msg": "OK"}