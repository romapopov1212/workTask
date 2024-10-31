from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.orders import Order
from database import get_session
from db import tables
from services.orders import OrderService

router = APIRouter(
    prefix='/orders',
)


@router.get('/', response_model=List[Order])
def get_orders(service: OrderService=Depends()):
    return service.get_list()


@router.get('/{order_id}', response_model=Order)
def get_orders_by_id(
    order_id:int,
    session: Session=Depends(get_session)
):
    order_one = (
        session
        .query(tables.Order)
        .filter(tables.Order.id == order_id)
        .first()
    )
    if order_one is None:
        raise HTTPException(status_code=404, detail="Order nor found")
    return order_one

#@router.post('/', response_model=Order)
#def create_order(
#        session: Session = Depends(get_session)
#):
