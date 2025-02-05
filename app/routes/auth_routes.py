from fastapi import APIRouter, Depends
from app.controllers.auth_controller import register_user, login_user
from app.schemas.user_schema import UserRegister, UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(data: UserRegister):
    return await register_user(data)

@router.post("/login")
async def login(data: UserLogin):
    return await login_user(data)
