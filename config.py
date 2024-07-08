from pydantic import BaseModel

from utils.config import BaseConfig


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


config = BaseConfig[ServiceConfig](file_path='./settings.toml', model_class=ServiceConfig)
