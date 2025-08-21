from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.security import hash_password
from src.schemas.user import UserCreateSchema, UserInDBSchema
from src.repositories.user_repository import UserRepository





class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    

    async def _get_or_404(self, user_id: int):
        user_obj = await self.user_repo.get_by_id(user_id)
        if not user_obj:
            raise HTTPException(status_code=404, detail="The User is not found")
        return user_obj

    

    async def get_user(self):
        return await self.user_repo.get_all()


    async def get_user_by_id(self, user_id: int):
        user_obj = await self._get_or_404(user_id)
        return user_obj

    async def update_user(self, user_id: int, user_data) -> None:
        if await self._get_or_404(user_id):
            await self.user_repo.update_by_id(user_id, user_data)


    async def delete_user(self, user_id) -> None:
        if await self._get_or_404(user_id):
            await self.user_repo.delete_by_id(user_id)



    async def register_user(self, user_data: UserCreateSchema):
        email_exists = await self.user_repo.get_user_by_email(user_data.email)

        if email_exists:
            raise HTTPException(status_code=401, detail="User with this email already exists")
        
        hashed_pwd = hash_password(user_data.password)

        user_create = UserInDBSchema(
            email=user_data.email,
            hashed_password=hashed_pwd,
            role="user"
        )

        await self.user_repo.create(user_create)
    

