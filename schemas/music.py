from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, AwareDatetime


class SongQuery(BaseModel):
    created_after: AwareDatetime | None = Field(default=None)
    created_before: AwareDatetime | None = Field(default=None)

    updated_after: AwareDatetime | None = Field(default=None)
    updated_before: AwareDatetime | None = Field(default=None)

    query: str | None = Field(default=None)

    pass


class DynamicMarking(Enum):
    PIANISSISSIMO = 0
    PIANISSIMO = 1
    PIANO = 2
    MEZZO_PIANO = 3
    MEZZO_FORTE = 4
    FORTE = 5
    FORTISSIMO = 6
    FORTISSISSIMO = 7


class TimeSignature:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper



class Staff:
    pass


class Clef(Enum):
    BASS = 'bass'
    TREBLE = 'treble'


class Accidental(Enum):
    FLAT = 'F'
    NATURAL = 'N'
    SHARP = 'S'


class Note(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'



class KeySignature:
    def __init__(self, accidentals: dict[Note, Accidental]):
        self.a = accidentals[Note.A]
        self.b = accidentals[Note.B]
        self.c = accidentals[Note.C]
        self.d = accidentals[Note.D]
        self.e = accidentals[Note.E]
        self.f = accidentals[Note.F]
        self.g = accidentals[Note.G]
        pass

class Measure(BaseModel):
    pass

class Track(BaseModel):
    clef: Clef
    key_signature: KeySignature
    time_signature: TimeSignature
    measures: list[Measure]
    pass

class SongBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID | None = Field(default=None)
    time_signature: TimeSignature = Field()
    clef: Clef = Field()
    track: Track = Field()
    name: str = Field(title="The name of the song", max_length=256)


class SongIn(SongBase):
    pass


class SongOut(SongBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: str
    updated_at: str
