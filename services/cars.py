from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db import tables
from database import get_session

class CarService:
    def __init__(self, session: Session=Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Car]:
        car = self.session.query(tables.Car).all()
        if car is None:
            raise HTTPException(status_code=404, detail='Not found')
        return car

    def get_by_id(self, car_id:int) ->tables.Car:
        car = self.session.query(tables.Car).filter(tables.Car.id == car_id).first()
        if car is None:
            raise HTTPException(status_code=404, detail='Not found')
        return car