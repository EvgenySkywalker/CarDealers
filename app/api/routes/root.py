from fastapi import APIRouter

from .dealer import router as dealer_router
from .car import router as car_router

router = APIRouter()

router.include_router(dealer_router, prefix='/dealers', tags=['dealers'])
router.include_router(car_router, prefix='/cars', tags=['cars'])
