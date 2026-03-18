from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes.home import home
from routes.books import books

app = FastAPI()

app.include_router(home)
app.include_router(books)

# connects to templates dir
# allows connection to template across all routes
app.state.templates = Jinja2Templates(directory="templates")