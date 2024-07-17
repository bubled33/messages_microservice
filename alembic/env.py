import os
import toml
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from src.models import Base

# Загрузка конфигурации из файла settings.toml
config_path = os.path.join('settings.toml')
config_data = toml.load(config_path)

# Формирование URL для подключения к базе данных
db_config = config_data['database']
db_url = f"postgresql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"

# Настройка конфигурации Alembic
alembic_config = context.config
alembic_config.set_main_option('sqlalchemy.url', db_url)

# Настройка логирования из файла конфигурации Alembic
fileConfig(alembic_config.config_file_name)

# Метаданные для целей автоматического создания таблиц
target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск миграций в оффлайн режиме.

    Использует URL для подключения к базе данных из конфигурации Alembic.
    """
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Запуск миграций в онлайн режиме.

    Использует движок SQLAlchemy для подключения к базе данных.
    """
    connectable = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Определение режима запуска миграций (онлайн или оффлайн)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
