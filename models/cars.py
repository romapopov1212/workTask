from pydantic import BaseModel


class Car(BaseModel):
    car_id: int
    name: str
    descriptions: str
    price: int
    class Config:
        orm_mode = True