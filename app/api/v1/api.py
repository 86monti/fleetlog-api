from fastapi import APIRouter

from app.api.v1.routes_users import router as users_router
from app.api.v1.routes_auth import router as auth_router
from app.api.v1.routes_vehicles import router as vehicles_router
from app.api.v1.routes_service_records import router as services_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(vehicles_router)
api_router.include_router(services_router)