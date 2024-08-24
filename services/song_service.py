from datetime import datetime

from fastapi import Depends
from odmantic.query import QueryExpression

from schemas.web import Page, PageRequest
from odmantic import AIOEngine, ObjectId

from configuration.mongo import engine, mongo_repo
from errors import NotFoundError
from models.music import Song
from schemas.music import SongIn, SongOut, SongQuery


def to_mongo_query(query: SongQuery) -> QueryExpression:
    Song.created_at.eq


class SongService:
    repo: AIOEngine = Depends(mongo_repo())

    def __init__(self, nosql: AIOEngine):
        self.nosql = nosql

    async def create_song(self, song: SongIn) -> ObjectId:
        now = datetime.now()

        # noinspection Pydantic
        return (await self.nosql.save(Song(**song.model_dump(), created_at=now, updated_at=now))).id

    async def read_song(self, id: ObjectId) -> SongOut:
        song = await self.nosql.find_one(Song, {'_id': id})
        if song is None:
            raise NotFoundError(Song, str(id))
        return SongOut(**song.model_dump())

    async def list_songs(self, query: SongQuery, page: PageRequest) -> Page[SongOut]:
        # construct criteria for matching

        queries = []

        songs = self.nosql.find(Song, *queries, skip=0, limit=100)
        total_elements = self.nosql.count(Song, {})

        return Page(content=songs, page=0, total_elements=total_elements, total_pages=1)
        pass

    async def update_song(self, id: ObjectId, song: SongIn):
        existing_song = await self.read_song(id)
        existing_song.model_update(**song.model_dump())

        now = datetime.now()
        existing_song.updated_at = now

        engine.save(existing_song)

        pass

    async def delete_song(self, id: ObjectId):
        song = await self.read_song(id)
        engine.delete(song)
        pass
