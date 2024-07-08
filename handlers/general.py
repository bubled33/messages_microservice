from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.routing import Router

from database.general import init_database

router = Router()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    yield
