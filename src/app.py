from contextlib import suppress

import uvicorn
from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

from src.config import config
from src.handlers import router
from src.handlers.general import lifespan


def create_app() -> FastAPI:
    """Создает и конфигурирует экземпляр приложения FastAPI.

    Returns:
        FastAPI: Настроенный экземпляр FastAPI.
    """
    app = FastAPI(lifespan=lifespan)
    app.include_router(router=router)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    return app


def run_server():
    """Запускает сервер Uvicorn с конфигурацией из файла config."""
    with suppress(KeyboardInterrupt):
        uvicorn.run(app, host=config.server.host, port=config.server.port, workers=config.server.workers)


# Основная точка входа приложения
if __name__ == '__main__':
    app = create_app()
    run_server()
