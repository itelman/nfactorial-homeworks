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
    new_book_id = len(books) + 1
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


@app.get("/books/{id}/edit")
def edit_book_form(request: Request, id: int):
    book = repository.get_one(id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")
    return templates.TemplateResponse("books/edit.html", {
        "request": request,
        "book": book
    })


@app.post("/books/{id}/edit")
async def update_book(
        id: int,
        title: str = Form(...),
        author: str = Form(...),
        year: int = Form(...),
        total_pages: int = Form(...),
        genre: str = Form(...)
):
    book = repository.get_one(id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    book.update({
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre,
    })

    return RedirectResponse(url=f"/books/{id}", status_code=302)


@app.post("/books/{id}/delete")
async def delete_book(id: int):
    book = repository.get_one(id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    repository.books = [b for b in repository.books if b["id"] != id]

    # Reassign IDs to keep sequence (optional)
    for idx, b in enumerate(repository.books, start=1):
        b["id"] = idx

    return RedirectResponse(url="/books", status_code=302)
