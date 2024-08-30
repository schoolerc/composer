import uuid
from typing import Optional, Annotated

from fastapi import Depends
from odmantic import AIOEngine

from configuration.mongo import mongo_repo
from models.music import Song


class SongRepo:
    def __init__(self, mongodb: Annotated[AIOEngine, Depends(mongo_repo)]):
        self.mongodb = mongodb

    async def find_by_id(self, song_id: uuid) -> Optional[Song]:
        return await self.mongodb.find_one(Song, Song.id == song_id)


    async def save(self, song: Song):
        await self.mongodb.save(song)
