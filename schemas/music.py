from odmantic import ObjectId
from pydantic import BaseModel, Field, ConfigDict, AwareDatetime


class SongQuery(BaseModel):
    created_after: AwareDatetime | None = Field(default=None)
    created_before: AwareDatetime | None = Field(default=None)

    updated_after: AwareDatetime | None = Field(default=None)
    updated_before: AwareDatetime | None = Field(default=None)

    query: str | None = Field(default=None)

    pass


class SongBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: ObjectId | None = Field(default=None)
    name: str = Field(title="The name of the song", max_length=256)


class SongIn(SongBase):
    pass


class SongOut(SongBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: str
    updated_at: str
