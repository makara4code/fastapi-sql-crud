from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# run only data not exist
models.Base.metadata.create_all(bind=engine)
