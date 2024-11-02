from datetime import timedelta, datetime
from http import HTTPStatus
from admin_info import username as AdminName
from admin_info import password as AdminPassword
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session as S
from starlette import status
from starlette.status import HTTP_401_UNAUTHORIZED

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
    if create_user_request.username == AdminName and create_user_request.password == AdminPassword:
        create_user_model = User(
            username=create_user_request.username,
            hashed_password = bcrypt_context.hash(create_user_request.password),
            is_admin = True
        )
    else:
        create_user_model = User(
            username=create_user_request.username,
            hashed_password=bcrypt_context.hash(create_user_request.password),
            is_admin=False
        )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return create_user_model

@router.post('/token', response_model=Token)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: S = db_dependency
):
    user = auth_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail='Не удалось подтвердить пользователя')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}

def auth_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
