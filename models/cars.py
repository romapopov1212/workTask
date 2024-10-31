from pydantic import BaseModel

class CarBase(BaseModel):
    name: str
    descriptions: str
    price: int

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True