from typing import List
from fastapi import APIRouter, Depends, Response, status

from models.cars import Car, CarCreate, CarUpdate
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

@router.put('/{car_id}', response_model=Car)
def update_car(car_id: int, car_data: CarUpdate, services: CarService = Depends()):
    return services.update(car_id, car_data)

@router.delete('/{car_id}')
def delete_car(car_id: int, services: CarService = Depends()):
    services.delete(car_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)