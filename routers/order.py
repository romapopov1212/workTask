from http.client import responses

from fastapi import APIRouter, HTTPException
from typing import List
from db.database import orders, cars_items
from db.schemas import OrderSchema, CreateOrderSchema
from db.models import Order
from routers.car import router

router= APIRouter(
    prefix="/orders"
)

@router.post("/", response_model=OrderSchema, summary="Создать заказ")
async def create_order(order_data: CreateOrderSchema):
    item = next((item for item in cars_items if item.id == order_data.car_id and item.available), None)
    if not item:
        return HTTPException(status_code=404, detail="Автомобиль не найден")

    total_price = order_data.quantity * item.price
    new_order = Order(id = len(orders)+1 , car_id = order_data.car_id, user_id = order_data.user_id, quantity = order_data.quantity, total_price = total_price)
    orders.append(new_order)
    return new_order

@router.get("/{order_id}", response_model=OrderSchema, summary="Получить информацию о заказе")
async def get_order(order_id: int):
    order = next((order for order in orders if order.id == order_id), None )
    if not order:
        return HTTPException(status_code=404, detail="Заказ не найден")
    return order

@router.get("/{user_id}", response_model=OrderSchema, summary="Получить информацию о всех заказах пользователя")
async def get_user_orders(user_id: int):
    user_orders = [order for order in orders if order.user_id == user_id]
    return user_orders