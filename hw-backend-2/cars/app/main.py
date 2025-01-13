from fastapi import FastAPI, Response, HTTPException

from cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)
@app.get("/cars")
def cars_pagination(page: int = 1, limit: int = 10):
    cars_paginated = {}

    for i in range(0, len(cars), limit):
        slice_key = i // limit + 1
        cars_paginated[slice_key] = cars[i:i + limit]

    return cars_paginated[page]


@app.get("/cars/{id}")
def cars_id(id: int):
    idx = id - 1
    if idx < 0 or idx >= cars.size():
        raise HTTPException(status_code=404, detail="Not Found")

    return cars[id - 1]

# (конец решения)
