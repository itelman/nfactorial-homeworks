from datetime import datetime, timedelta
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from base.models import UserResponse, TokenResponse, UserCreate, FlowerResponse, FlowerCreate
from repository.base import Base
from repository.flowers import FlowersRepository
from repository.users import UsersRepository

DATABASE_URL = "sqlite:///./storage.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SECRET_KEY = "zf5NgBhy6YvshK7o3kZ2VyQ9qJ8RvI41XTpLpXyz2qQ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signup", response_model=UserResponse)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    user_repo = UsersRepository(db)
    return user_repo.create_user(user_data)


@app.post("/login", response_model=TokenResponse)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user_repo = UsersRepository(db)
    user = user_repo.get_user_by_email(email)
    if not user or not pwd_context.verify(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = jwt.encode(
        {"sub": user.email, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}, SECRET_KEY,
        algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/flowers", response_model=List[FlowerResponse])
def get_flowers(db: Session = Depends(get_db)):
    flower_repo = FlowersRepository(db)
    return flower_repo.get_all_flowers()


@app.post("/flowers", response_model=FlowerResponse)
def add_flower(flower_data: FlowerCreate, db: Session = Depends(get_db)):
    flower_repo = FlowersRepository(db)
    return flower_repo.create_flower(flower_data)


@app.patch("/flowers/{flower_id}", response_model=FlowerResponse)
def update_flower(flower_id: int, flower_data: FlowerCreate, db: Session = Depends(get_db)):
    flower_repo = FlowersRepository(db)
    updated_flower = flower_repo.update_flower(flower_id, flower_data)
    if not updated_flower:
        raise HTTPException(status_code=404, detail="Flower not found")
    return updated_flower


@app.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    flower_repo = FlowersRepository(db)
    if not flower_repo.delete_flower(flower_id):
        raise HTTPException(status_code=404, detail="Flower not found")
    return {"message": "Flower deleted successfully"}


@app.get("/cart/items")
def get_cart_items():
    return {"message": "Cart items fetched"}
