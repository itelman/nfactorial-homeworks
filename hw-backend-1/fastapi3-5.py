from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, nfactorial!"}


@app.post("/meaning-of-life")
async def meaning_of_life():
    return {"meaning": "42"}

@app.get("/{num}")
async def read_factorial(num: int):
    return {"nfactorial": math.factorial(num)}