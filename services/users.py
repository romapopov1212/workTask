from typing import List

from starlette import status
from api.auth import SECRET_KEY, ALGORITHM
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import tables
from database import get_session
from jose import jwt, JWTError

class UserService:
    def __init__(self, session: Session=Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.User]:
        user = self.session.query(tables.User).all()
        if user is None:
            raise HTTPException(status_code=404, detail='Not found')
        return user

    # def get_user_by_token(self, token: str, db: Session = Depends(get_session)) -> tables.User:
    #     try:
    #
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         user_id: int = payload.get("user_id")
    #         if user_id is None:
    #             raise HTTPException(
    #                 status_code=status.HTTP_401_UNAUTHORIZED,
    #                 detail="Invalid token data",
    #             )
    #
    #
    #         user = db.query(tables.User).filter(tables.User.id == user_id).first()
    #         if user is None:
    #             raise HTTPException(
    #                 status_code=status.HTTP_401_UNAUTHORIZED,
    #                 detail="User not found",
    #             )
    #
    #         return user
    #
    #     except JWTError:
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Token has expired",
    #         )