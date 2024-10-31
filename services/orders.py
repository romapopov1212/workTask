from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import tables
from database import get_session

class OrderService:
    def __init__(self, session: Session=Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Order]:
        order = self.session.query(tables.Order).all()
        if order is None:
            raise HTTPException(status_code=404, detail='Not found')
        return order

