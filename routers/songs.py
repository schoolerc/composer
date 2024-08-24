from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.params import Query
from fastapi_utils.cbv import cbv

from schemas.web import PageRequest
from services.song_service import SongService
from schemas.web import Page, PageRequest
from schemas.music import SongOut, SongIn, SongQuery
from odmantic import ObjectId

router = APIRouter()


@cbv(router)
class SongRouter:
    song_service = Depends(SongService)

    @router.post("/song")
    async def create_song(self):
        pass

    @router.get("/song/{song_id}")
    async def read_song(self):
        pass

    @router.get("/songs")
    async def list_songs(self, query: Annotated[SongQuery, Query(default=SongQuery())]) -> Page[SongOut]:
        return await self.song_service.list_songs(query)

    @router.put("/song/{song_id}")
    async def update_song(self, song_id: ObjectId, song: Annotated[SongIn]):
        pass

    @router.delete("/song/{song_id}")
    async def delete_song(self):
        pass
