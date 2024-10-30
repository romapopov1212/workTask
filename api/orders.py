from typing import List

from attr import dataclass
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.orders import Order
from database import get_session
from db import orders

router = APIRouter(
    prefix='/orders',

)

@router.get('/', response_model=List[Order])
def get_orders(session: Session = Depends(get_session)):
    orders_list = session.query(orders.Order).all()
    if not orders_list:
        raise HTTPException(status_code=404, detail="No orders found")
    return orders_list

@router.get('/{order_id}', response_model=Order)
def get_orders_by_id(order_id:int, session: Session=Depends(get_session)):
    order_one = session.query(orders.Order).filter(orders.Order.order_id == order_id).first()
    if order_one is None:
        raise HTTPException(status_code=404, detail="Order nor found")
    return order_one