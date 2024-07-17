from src.config import config
from src.utils.logger import AsyncLogger

logger = AsyncLogger(**config.logger.dict())
