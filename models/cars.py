from pydantic import BaseModel

class CarBase(BaseModel):
    type: str
    model: str
    descriptions: str
    price: int

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

class CarCreate(CarBase):
    #в дальнейшем могут появиться поля
    pass
