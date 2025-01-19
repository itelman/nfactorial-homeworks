from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

comments = []

class Comment:
    def __init__(self, text: str, category: str):
        self.text = text
        self.category = category

@app.get("/", response_class=HTMLResponse)
async def read_feed(request: Request, page: int = 1, per_page: int = 5):
    start = (page - 1) * per_page
    end = start + per_page
    paginated_comments = comments[start:end]
    total_pages = (len(comments) + per_page - 1) // per_page
    return templates.TemplateResponse("index.html", {
        "request": request,
        "comments": paginated_comments,
        "page": page,
        "total_pages": total_pages
    })

@app.get("/comment/new", response_class=HTMLResponse)
async def comment_form(request: Request):
    return templates.TemplateResponse("comment_form.html", {"request": request})

@app.post("/comment/new")
async def add_comment(text: str = Form(...), category: str = Form(...)):
    new_comment = Comment(text=text, category=category)
    comments.insert(0, new_comment)
    return RedirectResponse(url="/", status_code=302)
