from database.db import book_coll
from models.book import Book, BookWithID
from bson import ObjectId

# used to run queries on db and pass to other modules

def return_all_books() -> list[Book] :
    books = []
    for book in book_coll.find():
        book["id"] = str(book["_id"])
        del book["_id"]
        books.append(BookWithID(**book))
    return books

def return_book_with_id(book_id: str) -> BookWithID:
    book_response = book_coll.find_one({"_id": ObjectId(book_id)})
    book_response["id"] = str(book_response["_id"])
    del book_response["_id"]
    return BookWithID(**book_response)

def add_book(book: Book):
    result = book_coll.insert_one(book.model_dump(exclude_none=True))
    book_response = BookWithID(id=str(result.inserted_id), **book.model_dump())
    return book_response