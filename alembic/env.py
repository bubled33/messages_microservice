import os
import toml
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from config import config
from database.models import Base

config_path = os.path.join('settings.toml')
config_data = toml.load(config_path)

db_config = config_data['database']
db_url = f"postgresql://{config.data.database.username}:{config.data.database.password}@{config.data.database.host}:{config.data.database.port}/{config.data.database.name}"

config = context.config
config.set_main_option('sqlalchemy.url', db_url)
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
