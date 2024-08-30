from datetime import datetime

from odmantic import Model, ObjectId, query

from schemas.music import Track


class Song(Model):
    name: str
    track: Track
    created_at: datetime
    updated_at: datetime


# noinspection Pydantic
query.eq(Song.name, "test")
