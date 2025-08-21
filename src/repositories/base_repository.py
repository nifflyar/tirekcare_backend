
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, db: AsyncSession, model):
        self.db = db
        self.model = model


    async def get_by_id(self, obj_id: int):
        result = await self.db.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalars().first()
    
    
    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        return result.scalar_one_or_none()



    async def get_all(self):
        stmt = select(self.model)
        result = await self.db.execute(stmt)
        return result.scalars().all()


    async def create(self, obj_data):
        obj = self.model(**obj_data.model_dump())
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    

    async def update(self, obj, obj_data):

        if hasattr(obj_data, "model_dump"): 
            obj_data = obj_data.model_dump()

        update_data = {k: v for k, v in obj_data.items() if v is not None}
        for key, value in update_data.items():
            setattr(obj, key, value)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    

    async def update_by_id(self, obj_id, obj_data):
        res = await self.db.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        obj = res.scalar_one_or_none()

        if hasattr(obj_data, "model_dump"): 
            obj_data = obj_data.model_dump()

        update_data = {k: v for k, v in obj_data.items() if v is not None}
        for key, value in update_data.items():
            setattr(obj, key, value)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    



    

    async def delete(self, obj):
        self.db.delete(obj)
        await self.db.commit()


    async def delete_by_id(self, obj_id):
        res = await self.db.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        obj = res.scalar_one_or_none()
        await self.db.delete(obj)
        await self.db.commit()