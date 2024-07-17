from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import config


async def init_database() -> async_sessionmaker[AsyncSession]:
    """Инициализирует асинхронное подключение к базе данных PostgreSQL.

    Формирует URL для подключения к базе данных, создает асинхронный движок
    SQLAlchemy и возвращает фабрику сессий для взаимодействия с базой данных.

    Returns:
        async_sessionmaker[AsyncSession]: Фабрика асинхронных сессий SQLAlchemy.
    """
    url = (
        f"postgresql+asyncpg://{config.database.username}:{config.database.password}"
        f"@{config.database.host}:{config.database.port}/{config.database.name}"
    )

    # Создание асинхронного движка SQLAlchemy
    engine = create_async_engine(
        url,
        echo=True,  # Включение логирования SQL-запросов
    )

    # Создание фабрики асинхронных сессий
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    return async_session
