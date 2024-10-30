from fastapi import APIRouter
from api.orders import router as operation_router
from api.cars import router as car_router
from api.users import router as  user_router
router = APIRouter()
router.include_router(operation_router)
router.include_router(car_router)
router.include_router(user_router)

