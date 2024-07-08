from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import config


async def init_database() -> async_sessionmaker[AsyncSession]:
    url = f"postgresql+asyncpg://{config.data.database.username}:{config.data.database.password}@{config.data.database.host}:{config.data.database.port}/{config.data.database.name}"
    engine = create_async_engine(
        url,
        echo=True,
    )

    async_session = async_sessionmaker(engine, expire_on_commit=False)

    return async_session
