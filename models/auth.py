from pydantic import BaseModel

class BaseUser(BaseModel):
    email:str
    username: str
