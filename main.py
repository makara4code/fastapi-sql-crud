from fastapi import FastAPI, status, Depends, HTTPException
import models
from database import engine, get_db
from models import Product
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()

# run only data not exist
models.Base.metadata.create_all(bind=engine)


class PostCreateRequest(BaseModel):
    name: str = Field(max_length=100)
    price: int
    rating: int = Field(ge=1, le=5)


db_dependency = Annotated[Session, Depends(get_db)]

# 1. db: Session = Depens(get_db) // old
# 2. db: Annotated[Session, Depends(get_db)] // new


# http://localhost:8000/products
@app.get("/products")
async def get_all_products(db: db_dependency):
    return db.query(Product).all()


@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: int, db: db_dependency):
    if product_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id should greater than 0"
        )

    product = db.query(Product).filter(Product.id == product_id).first()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    return product


@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_new_product(
    product_request: PostCreateRequest,
    db: db_dependency,
):
    # new_product = Product(
    #     name=product_request.name,
    #     price=product_request.price,
    #     rating=product_request.rating,
    # )

    new_product = Product(**product_request.model_dump())

    db.add(new_product)
    db.commit()


# By default fast api will return 200 status code if we don't specify status_code=status.HTTP_204_NO_CONTENT
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_by_id(product_id: int, db: db_dependency):
    if product_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id should greater than 0"
        )

    to_delete_product = db.query(Product).filter(Product.id == product_id).first()

    if to_delete_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="To be delete product not found",
        )

    # if record found
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
