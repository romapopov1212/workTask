from pydantic import BaseModel
from typing import List


class СarItemSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    available: str


class OrderSchema(BaseModel):
    id: int
    car_id: int
    user_id: int
    total_price: float


class CreateOrderSchema(BaseModel):
    user_id: int
    car_id: int
    quantity: int


