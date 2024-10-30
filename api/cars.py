from fastapi import APIRouter

router = APIRouter(
    prefix='/cars'
)

@router.get('/')
def get_cars():
    return []

@router.get('/{car_id}')
def get_cars_by_id(id: int):
    return []

