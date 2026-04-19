from pydantic import BaseModel, Field, ConfigDict, EmailStr
from models.book import Book


class User(BaseModel):
    username: str 
    email: EmailStr
    books: list[Book] = []

class UserWithID(User):
    id: str

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1)
    email: EmailStr | None = Field(default=None, min_length=1)
