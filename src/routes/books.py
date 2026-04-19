from fastapi import APIRouter, Request, HTTPException
from services.book_service import BookService

books = APIRouter()

# TODO: make user api

# routes to display books

#get individual book
@books.get("/{book_id}", include_in_schema=False)
async def book(request: Request, book_id: str):
    templates = request.app.state.templates
    book = BookService.return_book_with_id(book_id)
    return templates.TemplateResponse(request, "book.html",
                                          {"book": book})

# add book via post method

# delete book via id

# edit book via id

