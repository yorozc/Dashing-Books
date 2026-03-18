from database.db import book_coll
from models.book import Book, BookWithID
from bson import ObjectId

# used to run queries on db and pass to other modules

def return_all_books() -> list[BookWithID] :
    books = []
    for book in book_coll.find():
        book["id"] = str(book["_id"])
        del book["_id"]
        books.append(BookWithID(**book))
    # books = [BookWithID(**book) for book in book_coll.find()]
    print(books)
    return books

def add_book(book: Book):
    book_response = book_coll.insert_one(book.model_dump(exclude_none=True))
    return book_response