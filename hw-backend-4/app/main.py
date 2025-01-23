from typing import Optional

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import BooksRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = BooksRepository()
books = repository.get_all()

# Pagination settings
ITEMS_PER_PAGE = 10


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/books")
def get_books(request: Request, page: Optional[int] = 1):
    if page < 1:
        page = 1

    start_idx = (page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    paginated_books = books[start_idx:end_idx]

    return templates.TemplateResponse("books/index.html", {
        "request": request,
        "books": paginated_books,
        "page": page,
        "has_next": len(books) > end_idx,
        "has_prev": start_idx > 0,
    })


@app.get("/books/{id}")
def get_book_details(request: Request, id: int):
    book = repository.get_one(id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    return templates.TemplateResponse("books/details.html", {
        "request": request,
        "book": book,
    })


@app.get("/books/new")
async def new_book_form(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})


@app.post("/books")
async def create_book(
        title: str = Form(...),
        author: str = Form(...),
        year: int = Form(...),
        total_pages: int = Form(...),
        genre: str = Form(...)
):
    new_book_id = books.size() + 1
    new_book = {
        "id": new_book_id,
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre,
    }
    repository.save(new_book)

    return RedirectResponse(url=f"/books/{new_book_id}", status_code=302)
