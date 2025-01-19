from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Example car database
cars = [
    "BMW 7 Series",
    "BMW M5",
    "BMW 6 Series",
    "BMW M3",
    "BMW X1",
    "Audi A4",
    "Mercedes-Benz C-Class"
]

@app.get("/cars/search", response_class=HTMLResponse)
async def search_cars(request: Request, car_name: str = ""):
    filtered_cars = [car for car in cars if car_name.lower() in car.lower()]
    return templates.TemplateResponse("cars/search.html", {"request": request, "cars": filtered_cars, "car_name": car_name})

@app.get("/cars", response_class=HTMLResponse)
async def list_cars(request: Request):
    return templates.TemplateResponse("cars/list.html", {"request": request, "cars": cars})

@app.get("/cars/new", response_class=HTMLResponse)
async def new_car_form(request: Request):
    return templates.TemplateResponse("cars/new.html", {"request": request})

@app.post("/cars/new")
async def add_car(name: str = Form(...), year: int = Form(...)):
    cars.append(f"{name} ({year})")
    return RedirectResponse(url="/cars", status_code=302)