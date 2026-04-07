from fastapi import APIRouter, Request
from services.book_service import BookService

# creates app
home = APIRouter()

# index route, display books in db
@home.get("/", include_in_schema=False)
@home.get("/books", include_in_schema=False)
async def get_index(request: Request):
    templates = request.app.state.templates
    books = BookService.return_all_books()
    return templates.TemplateResponse(request, 
                                      "index.html",
                                      {"books": books})
    
