from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.auth import User
from models.orders import Order
from database import get_session
from db import tables
from services.auth import get_current_user
from services.orders import OrderService

router = APIRouter(
    prefix='/orders',
)


@router.get('/', response_model=List[Order])
def get_orders(user: User = Depends(get_current_user), service: OrderService=Depends()):
    return service.get_list(user_id=user.id)


@router.get('/{order_id}', response_model=Order)
def get_orders_by_id(
    order_id:int,
    session: Session=Depends(get_session),
    user: User = Depends(get_current_user)
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

