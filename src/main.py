from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes.home import home

app = FastAPI()

app.include_router(home)

# connects to templates dir
app.state.templates = Jinja2Templates(directory="templates")