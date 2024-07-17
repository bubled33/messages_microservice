import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ping(client):
    """
    Тестирует эндпоинт /api/base/ping.

    Проверяет, что эндпоинт возвращает статус 200 и корректный JSON-ответ.

    Args:
        client (AsyncClient): Асинхронный тестовый клиент.
    """
    response = await client.get("/api/base/ping")
    assert response.status_code == 200
    assert response.json() == {'result': 'pong'}
