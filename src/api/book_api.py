from models.book import Book, BookWithID
from services.book_service import (return_all_books, add_book, return_book_with_id)
from fastapi import APIRouter, HTTPException

# create crud functions for the books that return json

book_api = APIRouter()

@book_api.get("/api/books")
async def all_books() -> list[BookWithID]:
    books = return_all_books()
    return books

@book_api.get("/api/book/{book_id}")
async def book(book_id: str) -> BookWithID:
    return return_book_with_id(book_id)
    
# adds book to db
@book_api.post("/api/book")
async def book(book: Book) -> BookWithID:
    return add_book(book)


