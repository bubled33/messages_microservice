from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from starlette.requests import Request


def get_async_sessionmaker(request: Request) -> async_sessionmaker[AsyncSession]:
    """Получает фабрику асинхронных сессий из состояния приложения.

    Args:
        request (Request): Текущий запрос.

    Returns:
        async_sessionmaker[AsyncSession]: Фабрика асинхронных сессий.
    """
    return request.app.state.async_session_maker


async def get_session(
        async_session_maker: async_sessionmaker[AsyncSession] = Depends(get_async_sessionmaker)) -> AsyncSession:
    """Получает новую асинхронную сессию для взаимодействия с базой данных.

    Args:
        async_session_maker (async_sessionmaker[AsyncSession]): Фабрика асинхронных сессий.

    Yields:
        AsyncSession: Асинхронная сессия для выполнения операций с базой данных.
    """
    async with async_session_maker() as session:
        yield session
