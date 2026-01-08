from fastapi import APIRouter, Request
from better_auth.api.fastapi import get_current_user
from better_auth import Auth

router = APIRouter()


@router.post("/register")
async def register_user(request: Request, auth: Auth = Auth()):
    # Better Auth handles registration automatically
    return await auth.register(request)


@router.post("/login")
async def login_user(request: Request, auth: Auth = Auth()):
    # Better Auth handles login automatically
    return await auth.login(request)


@router.post("/logout")
async def logout_user(request: Request, auth: Auth = Auth()):
    # Better Auth handles logout automatically
    return await auth.logout(request)


@router.get("/me")
async def get_profile(user = get_current_user()):
    return user