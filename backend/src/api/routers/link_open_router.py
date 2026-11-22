
from fastapi import APIRouter

router = APIRouter()

@router.post("/api/open_link", tags=["core"])
def open_link(url: str):

    pass