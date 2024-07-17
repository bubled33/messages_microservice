import pytest
from httpx import AsyncClient

from src.app import app


@pytest.fixture(scope='module')
async def client():
    """
    Создает асинхронный клиент для тестирования FastAPI приложения.

    Returns:
        AsyncClient: Асинхронный тестовый клиент.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
