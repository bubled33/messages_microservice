from pydantic import BaseModel
from typing import Optional

from utils.config import BaseConfig
from utils.logger import AsyncLogger


class LoggerConfig(BaseModel):
    log_to_console: bool
    log_to_file: bool
    log_to_logstash: bool
    file_path: Optional[str]
    logstash_host: Optional[str]
    logstash_port: Optional[int]
    log_level: str


class Server(BaseModel):
    host: str
    port: int
    workers: int


class Database(BaseModel):
    host: str
    port: int
    username: str
    password: str
    name: str


class ServiceConfig(BaseModel):
    server: Server
    database: Database
    logger: LoggerConfig


config = BaseConfig[ServiceConfig](file_path='./settings.toml', model_class=ServiceConfig).data
logger = AsyncLogger(**config.logger.dict())
