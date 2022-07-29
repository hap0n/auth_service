from fastapi import APIRouter, HTTPException
from typing import List

from auth_service.repository.user_repository import UserRepository
from auth_service.router import schemas
from auth_service.service.user_service import UserService

user_router = APIRouter()


@user_router.post("/", response_model=schemas.user.User, tags=["users"])
async def create_user(user: schemas.user.UserDTO):
    db_user = UserRepository.get_user_by_username(user.username)
    if db_user:
        raise HTTPException(status_code=400, detail=f"User with username {user.username} already registered")
    return UserService.create_user(user)


@user_router.get("/", response_model=List[schemas.user.User], tags=["users"])
async def read_users(offset: int, limit: int):
    return UserRepository.get_users(offset=offset, limit=limit)


@user_router.get("/{username}/", response_model=schemas.user.User, tags=["users"])
async def read_user_by_username(username: str):
    maybe_user = UserRepository.get_user_by_username(username)
    if not maybe_user:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")
    return maybe_user
