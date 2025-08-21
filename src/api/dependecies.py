from typing import Annotated
from authx import RequestToken
from fastapi import Request, HTTPException

from src.core.security import auth_security, config





GetTokenDep = Annotated[RequestToken, auth_security.get_token_from_request]



async def get_current_user(request: Request):
    token = request.cookies.get(config.JWT_ACCESS_COOKIE_NAME)

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
        