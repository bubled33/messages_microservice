from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import config


async def init_database() -> async_sessionmaker[AsyncSession]:
    url = f"postgresql+asyncpg://{config.database.username}:{config.database.password}@{config.database.host}:{config.database.port}/{config.database.name}"
    engine = create_async_engine(
        url,
        echo=True,
    )

    async_session = async_sessionmaker(engine, expire_on_commit=False)

    return async_session
