from pydantic import BaseModel

class OrderBase(BaseModel):
    user_id: int
    price: int
class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True