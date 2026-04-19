from models.book import Book, BookWithID
from fastapi import APIRouter
from services.book_service import BookService

# create crud functions for the books that return json

book_api = APIRouter()

@book_api.get("/allBooks")
async def all_books() -> list[BookWithID]:
    books = BookService.return_all_books()
    return books

@book_api.get("/{book_id}")
async def book(book_id: str) -> BookWithID:
    return BookService.return_book_with_id(book_id)

@book_api.post("")
async def book(book: Book) -> BookWithID:
    return BookService.add_book(book)

@book_api.put("/{book_id}")
async def book(book_id: str, book: Book) -> Book:
    return BookService.edit_book(book_id, book)

@book_api.delete("/{book_id}")
async def book(book_id: str):
    return BookService.delete_book(book_id)


