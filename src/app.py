from contextlib import suppress

import uvicorn
from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

from src.config import config
from src.handlers import router
from src.handlers.general import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

app.add_middleware(GZipMiddleware, minimum_size=1000)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        uvicorn.run(app, host=config.server.host, port=config.server.port, workers=config.server.workers)
