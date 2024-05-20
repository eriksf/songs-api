import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config import settings

db_uri = f"{settings.db_protocol}://{settings.db_user}:{settings.db_password}@{settings.db_server}:{settings.db_port}/{settings.db_name}"

logger = logging.getLogger('uvicorn.error')

async_engine = create_async_engine(db_uri, echo=True)

logger.info(f"Connecting to {settings.db_protocol}://{settings.db_server}:{settings.db_port}/{settings.db_name}")


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(async_engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
