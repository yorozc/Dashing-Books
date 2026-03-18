from fastapi import APIRouter, Request

# creates app
home = APIRouter()

# index route, display books in db
@home.get("/", include_in_schema=False)
def get_index(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(request, "index.html")