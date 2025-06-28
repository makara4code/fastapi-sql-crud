from fastapi import FastAPI
from database import engine
import models

from routers import products, users, auth
from api.main import api_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# routes
# api version based on path parameter
# "/v1/*"
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(users.router)


# option 2:
# query parameter based
# "/products?version=1"
# "/products?version=2"

# option 3:
# header based
# "version: 1"
# "/products" with header "version: 1"

# option 4:
# subdomain based
# "v1.products.example.com"
# "v2.products.example.com"


# New Routes
app.include_router(api_router)
