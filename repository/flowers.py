from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from base.models import FlowerCreate
from repository.base import Base


class Flower(Base):
    __tablename__ = "flowers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)


class FlowersRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_flowers(self):
        return self.db.query(Flower).all()

    def create_flower(self, flower_data: FlowerCreate):
        flower = Flower(**flower_data.dict())
        self.db.add(flower)
        self.db.commit()
        self.db.refresh(flower)
        return flower

    def update_flower(self, flower_id: int, flower_data: FlowerCreate):
        flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return None
        for key, value in flower_data.dict().items():
            setattr(flower, key, value)
        self.db.commit()
        self.db.refresh(flower)
        return flower

    def delete_flower(self, flower_id: int):
        flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return None
        self.db.delete(flower)
        self.db.commit()
        return True
