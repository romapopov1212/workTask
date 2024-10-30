from fastapi import APIRouter

router = APIRouter(
    prefix='/orders',

)

@router.get('/')
def get_orders():
    return []

@router.get('/{order_id}')
def get_orders_by_id(id:int):
    return []