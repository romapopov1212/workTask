from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.cars import Car
from database import get_session
from db import cars
router = APIRouter(
    prefix='/cars'
)

@router.get('/', response_model=List[Car])
def get_cars(session: Session = Depends(get_session)): # внедрение зависимостей
    cars_list = session.query(cars.Car).all()
    if not cars_list:
        raise HTTPException(status_code=404, detail="No cars found")
    return cars_list

@router.get('/{car_id}')
def get_cars_by_id(id: int):

    return []

