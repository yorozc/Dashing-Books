from models.book import Book, BookWithID
from fastapi import APIRouter
from services.book_service import BookService

# create crud functions for the books that return json

book_api = APIRouter()

@book_api.get("/api/books")
async def all_books() -> list[BookWithID]:
    books = BookService.return_all_books()
    return books

@book_api.get("/api/book/{book_id}")
async def book(book_id: str) -> BookWithID:
    return BookService.return_book_with_id(book_id)

@book_api.post("/api/book")
async def book(book: Book) -> BookWithID:
    return BookService.add_book(book)

@book_api.put("/api/book/{book_id}")
async def book(book_id: str, book: Book) -> Book:
    return BookService.edit_book(book_id, book)

@book_api.delete("/api/book/{book_id}")
async def book(book_id: str):
    return BookService.delete_book(book_id)


