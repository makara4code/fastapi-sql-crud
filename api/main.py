from fastapi import APIRouter

from api.routes.v1 import users as v1_users
from api.routes.v1 import products as v1_products

from api.routes.v2 import users as v2_users
from api.routes.v2 import products as v2_products

api_router = APIRouter()

API_V1_STR: str = "/api/v1"
API_V2_STR: str = "/api/v2"

api_router.include_router(v1_users.router, prefix=API_V1_STR)
api_router.include_router(v1_products.router, prefix=API_V1_STR)

api_router.include_router(v2_users.router, prefix=API_V2_STR)
api_router.include_router(v2_products.router, prefix=API_V2_STR)
