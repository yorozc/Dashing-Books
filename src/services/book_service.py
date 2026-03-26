from database.db import book_coll
from models.book import Book, BookWithID
from bson import ObjectId
from fastapi import HTTPException

# used to run queries on db and pass to other modules

# add error handling
class BookService:
    def __init__():
        pass

    def return_all_books() -> list[Book]:
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

    def edit_book(book_id: str, book: Book):
        update_data = {k: v for k,v in book.model_dump(exclude_unset=True).items()}
        result = book_coll.find_one_and_update({"_id": ObjectId(book_id)},
                                    {"$set": update_data},
                                    return_document=True)
        if result is not None:
            return Book(**result)
        

    def delete_book():
        pass