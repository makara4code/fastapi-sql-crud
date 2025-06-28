from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users():
    return {"message": "List of users from v2"}


@router.post("/")
async def create_user():
    return {"message": "User created in v2"}
