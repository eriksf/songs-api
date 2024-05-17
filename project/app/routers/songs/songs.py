import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.routers.songs.models import Song, SongCreate, SongPublic
from app.utilities.db import get_session

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/{song_id}", response_model=SongPublic)
async def get_song(*, session: AsyncSession = Depends(get_session), song_id: int):
    song = await session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@router.get("", response_model=list[SongPublic])
async def get_songs(*, session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(Song))
    songs = results.scalars().all()
    return songs

@router.post("", response_model=SongPublic)
async def create_song(*, session: AsyncSession = Depends(get_session), song: SongCreate):
    db_song = Song.model_validate(song)
    session.add(db_song)
    await session.commit()
    await session.refresh(db_song)
    return db_song

@router.post("/batch")
async def create_songs_batch(*, session: AsyncSession = Depends(get_session), songs: list[SongCreate]):
    db_songs = [Song.model_validate(song) for song in songs]
    session.add_all(db_songs)
    await session.commit()
    return {"OK": True}
