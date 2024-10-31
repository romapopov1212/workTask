from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: str
    email: str
    hashed_password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True