from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import tables
from database import get_session

class OrderService:
    def __init__(self, session: Session=Depends(get_session)):
        self.session = session

    def get_list(self, user_id: int) -> List[tables.Order]:
        query = (
            self.session
            .query(tables.Order)
            .filter_by(user_id=user_id)
        )
        car = query.all()
        return car

#    def create(self, user_id: int, operation_data: ) -> tables.Order:

