from fastapi import HTTPException, APIRouter
from typing import List
from db.database import cars_items
from db.models import CarItem
from db.schemas import СarItemSchema


router = APIRouter(
    prefix= "/car",

)

@router.get("/", response_model=List[СarItemSchema], summary="Получить список техники")
def get_car_items():
    return cars_items


@router.get("/{item_id}", response_model=СarItemSchema, summary="Получить информацию о конкретной техники")
def get_car_item(item_id: int):
    item = next((item for item in cars_items if item.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Техника не найдена")
    return item