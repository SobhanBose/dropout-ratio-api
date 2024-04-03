from fastapi import APIRouter, status, HTTPException

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def home():
    raise HTTPException(status_code=status.HTTP_200_OK)