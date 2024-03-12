from fastapi import APIRouter

from .controller.electricity_reading_controller import router as reading_router
from .controller.price_plan_comparator_controller import router as price_plan_router
from .system.routes import router as system_router

api_router = APIRouter()

api_router.include_router(reading_router)
api_router.include_router(price_plan_router)
api_router.include_router(system_router)
