from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes.home import home
from routes.books import books
from api.book_api import book_api

app = FastAPI()

app.include_router(home)
app.include_router(books)

# external api
app.include_router(book_api)

# connects to templates dir
# allows connection to template across all routes
app.state.templates = Jinja2Templates(directory="templates")