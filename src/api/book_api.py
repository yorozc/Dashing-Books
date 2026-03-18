from models.book import Book
from services.book_service import (return_all_books, add_book)
from fastapi import APIRouter, HTTPException

# create crud functions for the books that return json

book_api = APIRouter()

@book_api.get("/api/books")
async def all_books():
    books = return_all_books()
    return books
    

# adds book to db
@book_api.post("/api/book")
async def book(book: Book) -> Book:
    add_book(book)
    return book


