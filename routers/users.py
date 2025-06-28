from fastapi import APIRouter


router = APIRouter()


@router.get("/users/")
async def get_all_users():
    return {"message": "This endpoint will return all users."}
