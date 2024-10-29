from pydantic import BaseModel

class CarItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    available: bool

class Order(BaseModel):
    id: int
    car_id: int
    user_id: int
    total_price: float



