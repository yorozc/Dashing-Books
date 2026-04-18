from pydantic import BaseModel, Field, ConfigDict

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1)
    # description: str
    #isbn

class BookWithID(Book):
    id: str

class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    author: str | None = Field(default=None, min_length=1)

# class BookResponse(BookWithID):
#     model_config = ConfigDict(from_attributes=True)

#     date_posted: str