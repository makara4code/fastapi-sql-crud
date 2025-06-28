from fastapi import APIRouter


router = APIRouter()


@router.post("/v1/auth/token")
async def get_token_v1():
    return {"message": "This endpoint will return token."}


@router.post("/v2/auth/token")
async def get_token_v2():
    return {"message": "This endpoint will return token."}
