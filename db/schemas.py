from pydantic import BaseModel
from typing import List


class СarItemSchema(BaseModel):
    id: int
    name: str
    description: str
    price: int
    available: str


class OrderSchema(BaseModel):
    id: int
    car_id: int
    user_id: int
    total_price: int


class CreateOrderSchema(BaseModel):
    user_id: int
    car_id: int
    quantity: int


