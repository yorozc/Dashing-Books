from models.book import Book, BookWithID
from models.user import User, UserWithID, UserUpdate
from fastapi import APIRouter
from services.user_service import UserService


user_api = APIRouter()

@user_api.get("/{user_id}")
async def get_user(user_id: str) -> UserWithID:
    return UserService.get_user(user_id)

@user_api.post("")
async def post_user(user: User) -> UserWithID:
    return UserService.create_user(user)

@user_api.patch("/{user_id}")
async def edit_user(user_id: str, user: UserUpdate):
    return UserService.edit_user(user_id, user)

@user_api.delete("/{user_id}")
async def delete_user(user_id: str):
    return UserService.delete_user(user_id)