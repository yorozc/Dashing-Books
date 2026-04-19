from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import RedirectResponse
from services.book_service import BookService
from models.book import Book

books = APIRouter()

# routes to display books

# show book form and add book via form using post method
# add name argument for url_for()
@books.get("/addBook", include_in_schema=False, name="show_add_book")
async def show_add_book(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(request=request, name="addBook.html")

@books.post("/addBook", include_in_schema=False)
async def add_book(request: Request,
                   title: str = Form(...),
                   author: str = Form(...)):
    # create data into form required to add to DB
    book = {
        "title": title,
        "author": author
    }
    # wrap dict in Book and unwrap dict 
    BookService.add_book(Book(**book)) 
    return RedirectResponse(url="/", status_code=303)

#get individual book
@books.get("/{book_id}", include_in_schema=False)
async def get_book(request: Request, book_id: str):
    templates = request.app.state.templates
    book = BookService.return_book_with_id(book_id)
    return templates.TemplateResponse(request, "book.html",
                                          {"book": book})

# delete book via id
# can't use delete with plain html, simulate with post
@books.post("/{book_id}/delete", include_in_schema=False)
async def delete_book(book_id: str):
    BookService.delete_book(book_id)
    return RedirectResponse(url="/", status_code=303)

# edit book via id

