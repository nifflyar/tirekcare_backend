from src.db.database import async_engine, Base
import src.models


async def drop_create_db():
 async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        