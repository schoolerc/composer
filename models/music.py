from datetime import datetime

from odmantic import Model, ObjectId, query


class Song(Model):
    name: str
    created_at: datetime
    updated_at: datetime


# noinspection Pydantic
query.eq(Song.name, "test")
