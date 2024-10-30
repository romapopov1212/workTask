from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    surname: str
    email: str
    hashed_password: str
    class Config:
        orm_mode = True