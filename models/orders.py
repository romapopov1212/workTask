from pydantic import BaseModel


class Order(BaseModel):
    order_id: int
    user_id: int
    price: int
    class Config:
        orm_mode = True