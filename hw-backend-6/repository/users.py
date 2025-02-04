import uuid
from typing import Optional

from passlib.hash import bcrypt


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
