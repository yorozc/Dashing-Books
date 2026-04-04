from fastapi import APIRouter, Request, HTTPException
from services.book_service import BookService

books = APIRouter()

# routes to display books

@books.get("/books/{book_id}", include_in_schema=False)
async def book(request: Request, book_id: str):
    templates = request.app.state.templates
    book = BookService.return_book_with_id(book_id)
    if book:
        return templates.TemplateResponse(request, "book.html",
                                          {"book": book})
    
    raise HTTPException(status_code=404, detail="Book not found!")