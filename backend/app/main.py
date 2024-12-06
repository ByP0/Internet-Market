from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.app.routers.users import router as users_router
from backend.app.routers.auth import router as auth_router
from backend.app.database import create_tables
from backend.app.main_models import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(auth_router)