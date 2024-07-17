from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.routing import Router

from src.database import init_database

router = Router()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.async_session_maker = await init_database()

    yield
