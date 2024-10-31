from datetime import timedelta, datetime
from symtable import Class
from sys import prefix
from termios import CREAD
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from jose.constants import ALGORITHMS
from passlib.handlers.bcrypt import bcrypt
from pydantic import BaseModel
from sqlalchemy.orm import Session as S
from sqlalchemy.util import deprecated
from starlette import status
from database import Session
from models.users import UserResponse
from db.tables import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from database import get_session

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = '7oHQyjS2lQIcK7k1pfyWE0KnywC3fp2O'
ALGORITHM = 'HS256'
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
oauth_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


db_dependency = Depends(get_session)
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(create_user_request: CreateUserRequest, db: S = db_dependency ):
    create_user_model = User(
        username=create_user_request.username,
        hashed_password = bcrypt_context.hash(create_user_request.password)
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return create_user_model