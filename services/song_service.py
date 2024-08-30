from datetime import datetime
from typing import Annotated

from fastapi import Depends
from odmantic import ObjectId

from configuration.mongo import engine
from errors import NotFoundError
from models.music import Song
from repo.music import SongRepo
from schemas.music import SongIn, SongOut, SongQuery
from schemas.web import Page, PageRequest

# replace with uuid7 when merged
from uuid import uuid4 as uuid, UUID


class SongService:

    def __init__(self, song_repo: Annotated[SongRepo, Depends(SongRepo)]):
        self.song_repo = song_repo

    async def create_song(self, song: SongIn) -> UUID:
        now = datetime.now()
        song_id = uuid()

        persisted_song = Song(**song.model_dump(), created_at=now, updated_at=now)
        persisted_song.id = song_id
        await self.song_repo.save(persisted_song)
        return song_id

    async def read_song(self, song_id: UUID) -> SongOut:
        persisted_song = await self.song_repo.find_by_id(song_id)
        if persisted_song is None:
            raise NotFoundError(resource_type=Song, resource_id=song_id)

        return SongOut(**persisted_song.model_dump())

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
