from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)
@app.get("/users")
def users_all(request: Request, page: int = 1, limit: int = users.size()):
    # return templates.TemplateResponse("users/index.html", {"request": request, "users": users})

    users_paginated = {}

    for i in range(0, len(users), limit):
        slice_key = i // limit + 1
        users_paginated[slice_key] = users[i:i + limit]

    return templates.TemplateResponse("users/index.html", {"request": request, "users": users_paginated[page]})


@app.get("/users/{id}")
def users_id(id: int, request: Request):
    idx = id - 1
    if idx < 0 or idx >= users.size():
        raise HTTPException(status_code=404, detail="Not Found")

    user = users[id - 1]
    return templates.TemplateResponse("users/user.html", {"request": request, "user": user})

# (конец решения)
