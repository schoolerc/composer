from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Body

from schemas.music import SongOut, SongIn, SongQuery
from schemas.web import Page
from schemas.web import PageRequestDep
from services.song_service import SongService

song_router = APIRouter()


@song_router.post("/song")
async def create_song(song_service: Annotated[SongService, Depends(SongService)],
                      song: Annotated[SongIn, Body(title="The song to create")]) -> UUID:
    return await song_service.create_song(song)


@song_router.get("/song/{song_id}")
async def read_song(song_id: Annotated[UUID, Path(title="The ID of the song to read")]) -> SongOut:
    pass


@song_router.get("/songs")
async def list_songs(self, query: Annotated[SongQuery, Depends(SongQuery)],
                     page_request: PageRequestDep) -> Page[SongOut]:
    pass


@song_router.put("/song/{song_id}")
async def update_song(song_id: Annotated[UUID, Path(title="The ID of the song to update")],
                      song: Annotated[SongIn, Body()]):
    pass


@song_router.delete("/song/{song_id}")
async def delete_song(song_id: Annotated[UUID, Path(title="The ID of the song to delete")]):
    pass
