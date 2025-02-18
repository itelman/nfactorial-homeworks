from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    name: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    name: str


class FlowerCreate(BaseModel):
    name: str
    quantity: int
    price: int


class FlowerResponse(BaseModel):
    id: int
    name: str
    quantity: int
    price: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
