from fastapi import FastAPI
from database import engine
import models

from routers import products, users, auth
from api.main import api_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Old Routes
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(users.router)


# New Routes
app.include_router(api_router)