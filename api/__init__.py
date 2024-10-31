from fastapi import APIRouter
from api.orders import router as order_router
from api.cars import router as car_router
from api.users import router as  user_router
from api.auth import router as auth_user_cuter
router = APIRouter()
router.include_router(order_router)
router.include_router(car_router)
router.include_router(user_router)
router.include_router(auth_user_cuter)
