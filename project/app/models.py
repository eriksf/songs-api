from sqlmodel import Field, SQLModel


class SongBase(SQLModel):
    name: str
    artist: str
    year: int | None = None


class Song(SongBase, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)


class SongCreate(SongBase):
    pass


class SongPublic(SongBase):
    id: int
