from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/")
async def products():
    return {"message": "List of product from v2"}


@router.post("/")
async def create_product():
    return {"message": "Product created in v2"}
