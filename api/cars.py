from typing import List
from fastapi import APIRouter, Depends

from models.cars import Car, CarCreate
from services.cars import CarService

router = APIRouter(
    prefix='/cars'
)


@router.get('/', response_model=List[Car])
def get_cars(services: CarService = Depends()): # внедрение зависимостей
    return services.get_list()


@router.get('/{car_id}', response_model=Car)
def get_cars_by_id(
        car_id: int,
        service: CarService=Depends()
):
    return service.get_by_id(car_id)

@router.post('/', response_model=Car)
def create_car(car_data : CarCreate, services: CarService = Depends()):
    return services.create(car_data)