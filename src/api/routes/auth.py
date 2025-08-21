from fastapi import APIRouter, Depends, Response
from authx import RequestToken


from src.api.dependecies import GetTokenDep
from src.db.dependencies import DbSessionDep
from src.core.security import auth_security
from src.services.auth_service import AuthService
from src.services.user_service import UserService
from src.schemas.user import UserCreateSchema, UserLoginSchema
from src.tasks.email import send_verification_code

router = APIRouter(prefix="/auth", tags=["Auth"])





@router.post("/register", description="Register a user")
async def user_registration(db: DbSessionDep, user: UserCreateSchema):
    user_service = UserService(db)
    await user_service.register_user(user_data=user)
    return {"msg" : "User has been added"}



@router.post("/login", description="Login into account")
async def user_login(db: DbSessionDep, creds: UserLoginSchema, response: Response):
    auth_service = AuthService(db)
    return await auth_service.login(user_data=creds, response=response)


@router.post("/logout", description="Logout from account")
async def user_logout(db: DbSessionDep, creds: UserLoginSchema, response: Response):
    auth_service = AuthService(db)
    return await auth_service.logout(response=response)