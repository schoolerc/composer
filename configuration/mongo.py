from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict()

    mongo_host: str = 'localhost'
    mongo_port: int = 27017
    mongo_database: str = 'composer'


settings = MongoSettings()
engine = AIOEngine(AsyncIOMotorClient(settings.mongo_host, settings.mongo_port), settings.mongo_database)


def mongo_repo():
    return engine
