from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    hashed_password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
