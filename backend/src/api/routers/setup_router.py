
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/setup", tags=["setup"])
def setup_computers():
    pass