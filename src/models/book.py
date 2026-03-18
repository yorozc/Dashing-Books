from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    # description
    #isbn

class BookWithID(Book):
    id: int