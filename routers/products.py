from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from models import Product
from pydantic import BaseModel, Field
from typing import Optional


class ProductCreateRequest(BaseModel):
    name: str = Field(max_length=100)
    price: int
    rating: int = Field(ge=1, le=5)


class ProductPatchRequest(BaseModel):
    name: Optional[str] = Field(max_length=100, default=None)
    price: Optional[int] = Field(default=None)
    rating: Optional[int] = Field(ge=1, le=5, default=None)


router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


# http://localhost:8000/products
@router.get("/products/")
async def get_all_products(db: db_dependency):
    return db.query(Product).all()


@router.get("/products/{product_id}", status_code=status.HTTP_200_OK)
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


@router.post("/products/", status_code=status.HTTP_201_CREATED)
async def create_new_product(
    product_request: ProductCreateRequest,
    db: db_dependency,
):
    new_product = Product(**product_request.model_dump())

    db.add(new_product)
    db.commit()


@router.put("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_product_by_id(
    db: db_dependency, product_id: int, product: ProductCreateRequest
):
    # product_db = db.query(Product).filter(Product.id == product_id).first()

    db.query()
    query = select(Product).where(Product.id == product_id)
    result = db.scalars(query).first()

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    result.name = product.name  # type: ignore
    result.price = product.price  # type: ignore
    result.rating = product.rating  # type: ignore

    db.add(result)
    db.commit()


@router.patch("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def patch_product_by_id(
    db: db_dependency, product_id: int, product: ProductPatchRequest
):
    # TODO: convert below code into v2 query
    product_from_db = db.query(Product).filter(Product.id == product_id).first()

    if product_from_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    product_from_user = product.model_dump(exclude_none=True)

    for key, value in product_from_user.items():
        setattr(product_from_db, key, value)

    db.add(product_from_db)
    db.commit()


# By default fast api will return 200 status code if we don't specify status_code=status.HTTP_204_NO_CONTENT
@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
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
