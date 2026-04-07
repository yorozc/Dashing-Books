from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from routes.home import home
from routes.books import books
from api.book_api import book_api

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home)
app.include_router(books)

# external api
app.include_router(book_api)

# connects to templates dir
# allows connection to template across all routes
app.state.templates = Jinja2Templates(directory="templates")
template = Jinja2Templates(directory="templates")

# exception handler for http errors
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (exception.detail
               if exception.detail
               else "An error occurred. Please check your request and try again.")
    
    if request.url.path.startswith("/api"): # deals with external facing api
        return JSONResponse(status_code=exception.status_code, content={"detail": message})
    
    # for template responses
    return template.TemplateResponse(request, "error.html",
                                            {
                                                "status_code": exception.status_code,
                                                "title": exception.status_code,
                                                "message": message,
                                            },
                                            status_code=exception.status_code)

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    
    return template.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )
