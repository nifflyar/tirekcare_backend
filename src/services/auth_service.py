from fastapi import HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.user import UserLoginSchema
from src.repositories.auth_repository import AuthRepository
from src.core.security import verify_password, auth_security, config


class AuthService:
    def __init__(self, db: AsyncSession):
        self.auth_repo = AuthRepository(db)
    


    async def login(self, user_data: UserLoginSchema, response: Response):
        user_obj = await self.auth_repo.get_user_by_email(user_data.email)

        if user_obj and verify_password(user_data.password, user_obj.hashed_password):
            token = auth_security.create_access_token(uid=str(user_obj.id))

            response.set_cookie(
                key=config.JWT_ACCESS_COOKIE_NAME,
                value=token,
                httponly=True,
                secure=False,
                samesite="lax",
                max_age=1800,
            )

            return {"token" : token}
        
        raise HTTPException(status_code=401, detail="Incorrect email or password")


    async def logout(self, response: Response):
        response.delete_cookie(
            key=config.JWT_ACCESS_COOKIE_NAME,
            httponly=True,
            secure=False,
            samesite="lax")
        return {"msg": "Logged out"}
