import uvicorn
from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

from config import config
from handlers import router
from handlers.general import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

app.add_middleware(GZipMiddleware, minimum_size=1000)

if __name__ == '__main__':
    uvicorn.run(app, host=config.data.server.host, port=config.data.server.port, workers=config.data.server.workers)
