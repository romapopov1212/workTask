from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    hashed_password: str
    is_admin: bool
class User(UserBase):
    id: int
    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    username: str
    is_admin: bool
    class Config:
        orm_mode = True
