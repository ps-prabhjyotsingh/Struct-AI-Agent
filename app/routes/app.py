from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"status":True, "message":"Accepting requests"}