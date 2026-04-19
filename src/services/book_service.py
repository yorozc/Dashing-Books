from database.db import book_coll
from models.book import Book, BookWithID, BookUpdate
from bson import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument

# used to run queries on db and pass to other modules

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
        try:
            book_response = book_coll.find_one({"_id": ObjectId(book_id)})
        except Exception as e:
            raise HTTPException(status_code=422, detail="Not a valid ID")
        
        if book_response is None: 
            raise HTTPException(status_code=404, detail="Book not found")
        
        book_response["id"] = str(book_response["_id"])
        del book_response["_id"]
        return BookWithID(**book_response)

    def add_book(book: Book):
        result = book_coll.insert_one(book.model_dump(exclude_none=True))
        book_response = BookWithID(id=str(result.inserted_id), **book.model_dump())
        return book_response

    def edit_book(book_id: str, book: BookUpdate):
        try:
            update_data = book.model_dump(exclude_unset=True)
            result = book_coll.find_one_and_update({"_id": ObjectId(book_id)},
                                        {"$set": update_data},
                                        return_document=ReturnDocument.AFTER)
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"{e}")
        
        if result is not None:
            return Book(**result)
        raise HTTPException(status_code=404, detail="Book not found")
        
    def delete_book(book_id: str):
        try:
            del_result = book_coll.find_one_and_delete({"_id": ObjectId(book_id)})
        except Exception as e:
            raise HTTPException(status_code=422, detail="Not a valid ID")

        if del_result is not None:
            return Book(**del_result)
        raise HTTPException(status_code=404, detail="Book not found")