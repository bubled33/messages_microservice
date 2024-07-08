from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from starlette.requests import Request


def get_async_sessionmaker(request: Request) -> async_sessionmaker[AsyncSession]:
    return request.app.state.async_session_maker


async def get_session(
        async_session_maker: async_sessionmaker[AsyncSession] = Depends(get_async_sessionmaker)) -> AsyncSession:
    async with async_session_maker() as session:
        yield session
