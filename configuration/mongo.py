from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict()

    mongo_dsn = MongoDsn
    mongo_database: str


settings = MongoSettings()
engine = AIOEngine(AsyncIOMotorClient(settings.mongo_dsn), settings.mongo_database)


def mongo_repo():
    return engine


