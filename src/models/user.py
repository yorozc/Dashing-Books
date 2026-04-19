from pydantic import BaseModel, Field, ConfigDict, EmailStr


class User(BaseModel):
    username: str 
    email: EmailStr
    books: list

class UserWithID(User):
    id: str