from models.book import Book, BookWithID, BookUpdate
from fastapi import APIRouter
from services.book_service import BookService

# create crud functions for the books that return json

book_api = APIRouter()

@book_api.get("")
async def all_books() -> list[BookWithID]:
    books = BookService.return_all_books()
    return books

@book_api.get("/{book_id}")
async def get_book(book_id: str) -> BookWithID:
    return BookService.return_book_with_id(book_id)

@book_api.post("")
async def post_book(book: Book) -> BookWithID:
    return BookService.add_book(book)

@book_api.patch("/{book_id}")
async def patch_book(book_id: str, book: BookUpdate) -> Book:
    return BookService.edit_book(book_id, book)

@book_api.delete("/{book_id}")
async def del_book(book_id: str):
    return BookService.delete_book(book_id)


