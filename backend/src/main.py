from fastapi import FastAPI
from api.routers.link_open_router import router as link_router
from fastapi import FastAPI
from api.routers.link_open_router import router as link_router
from api.routers.setup_router import router as setup_router

app = FastAPI()

app.include_router(link_router)
app.include_router(setup_router)

@app.get("/")
def root():
    return {}

