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

@router.get('/{car_id}', response_model=Car)
def get_cars_by_id(car_id: int, session: Session = Depends(get_session)):
    car_one = session.query(cars.Car).filter(cars.Car.car_id == car_id).first()
    if car_one is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car_one

