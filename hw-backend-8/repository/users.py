from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from base.models import UserCreate
from repository.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)


class UsersRepository:
    def __init__(self, db: Session, pwd_context: CryptContext):
        self.db = db
        self.pwd_context = pwd_context

    def create_user(self, user_data: UserCreate):
        hashed_password = self.pwd_context.hash(user_data.password)
        user = User(email=user_data.email, name=user_data.name, password_hash=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
