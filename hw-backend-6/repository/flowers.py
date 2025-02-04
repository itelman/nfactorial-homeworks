import uuid
from typing import Optional


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
