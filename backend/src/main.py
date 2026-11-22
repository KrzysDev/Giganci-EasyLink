from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.link_open_router import router as link_router
from api.routers.setup_router import router as setup_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(link_router)
app.include_router(setup_router)


@app.get("/")
def root():
    return {}