from fastapi import APIRouter, Request, HTTPException, Form
from services.book_service import BookService

books = APIRouter()

# routes to display books

# show book form and add book via form using post method
# add name argument for url_for()
@books.get("/addBook", include_in_schema=False, name="show_add_book")
async def show_add_book(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(request=request, name="addBook.html")

@books.post("/addBook", include_in_schema=False)
async def add_book(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(request, "addBook.html")

#get individual book
@books.get("/{book_id}", include_in_schema=False)
async def get_book(request: Request, book_id: str):
    templates = request.app.state.templates
    book = BookService.return_book_with_id(book_id)
    return templates.TemplateResponse(request, "book.html",
                                          {"book": book})



# delete book via id

# edit book via id

