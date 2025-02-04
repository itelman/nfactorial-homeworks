import uuid
from typing import Optional

from fastapi import FastAPI, Form, Request, Cookie, Depends, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from jose import jwt, JWTError
from passlib.hash import bcrypt

app = FastAPI()
templates = Jinja2Templates(directory="templates")

SECRET_KEY = "zf5NgBhy6YvshK7o3kZ2VyQ9qJ8RvI41XTpLpXyz2qQ"
ALGORITHM = "HS256"


class User:
    def __init__(self, email: str, name: str, password: str):
        self.id = uuid.uuid4()
        self.email = email
        self.name = name
        self.password = bcrypt.hash(password)
        self.purchased = []


class UsersRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email == email), None)


users_repo = UsersRepository()


class Flower:
    def __init__(self, name: str, quantity: int, price: float):
        self.id = uuid.uuid4()
        self.name = name
        self.quantity = quantity
        self.price = price


class FlowersRepository:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    def get_flower_by_id(self, flower_id: uuid.UUID) -> Optional[Flower]:
        return next((flower for flower in self.flowers if flower.id == flower_id), None)


flowers_repo = FlowersRepository()


# Helper functions
def authenticate_user(email: str, password: str) -> Optional[User]:
    user = users_repo.get_user_by_email(email)
    if user and bcrypt.verify(password, user.password):
        return user
    return None


def get_current_user(token: str = Cookie(None)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = users_repo.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=403, detail="Invalid authentication credentials")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")


# Routes
@app.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup")
async def signup(email: str = Form(...), name: str = Form(...), password: str = Form(...)):
    if users_repo.get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Email already exists")
    user = User(email, name, password)
    users_repo.add_user(user)
    return RedirectResponse(url="/login", status_code=302)


@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    token = jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)
    response = RedirectResponse(url="/profile", status_code=302)
    response.set_cookie(key="token", value=token)
    return response


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request, user: User = Depends(get_current_user)):
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})


@app.get("/flowers", response_class=HTMLResponse)
async def flowers_list(request: Request):
    return templates.TemplateResponse("flowers.html", {"request": request, "flowers": flowers_repo.flowers})


@app.post("/flowers")
async def add_flower(name: str = Form(...), quantity: int = Form(...), price: float = Form(...)):
    flower = Flower(name, quantity, price)
    flowers_repo.add_flower(flower)
    return RedirectResponse(url="/flowers", status_code=302)


@app.post("/cart/items")
async def add_to_cart(flower_id: uuid.UUID = Form(...), cart: str = Cookie("")):
    cart_items = cart.split(",") if cart else []
    cart_items.append(str(flower_id))
    response = RedirectResponse(url="/flowers", status_code=302)
    response.set_cookie(key="cart", value=",".join(cart_items))
    return response


@app.get("/cart/items", response_class=HTMLResponse)
async def cart_items(request: Request, cart: str = Cookie("")):
    cart_items = cart.split(",") if cart else []
    flowers_in_cart = [flowers_repo.get_flower_by_id(uuid.UUID(f)) for f in cart_items if f]
    total_price = sum(f.price for f in flowers_in_cart if f)
    return templates.TemplateResponse("cart.html",
                                      {"request": request, "flowers": flowers_in_cart, "total": total_price})


@app.post("/purchased")
async def purchase(cart: str = Cookie(""), user: User = Depends(get_current_user)):
    cart_items = cart.split(",") if cart else []
    user_purchased = getattr(user, "purchased", [])
    user_purchased.extend(cart_items)
    user.purchased = user_purchased
    response = RedirectResponse(url="/purchased", status_code=302)
    response.delete_cookie(key="cart")
    return response


@app.get("/purchased", response_class=HTMLResponse)
async def purchased_flowers(request: Request, user: User = Depends(get_current_user)):
    purchased_flowers = [flowers_repo.get_flower_by_id(uuid.UUID(f)) for f in user.purchased]
    return templates.TemplateResponse("purchased.html", {"request": request, "flowers": purchased_flowers})
