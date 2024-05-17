import logging

import uvicorn
from fastapi import FastAPI

from app.config import settings
from app.routers.songs import songs
from app.routers.status import status

description = """
This is an API for Songs built with [FastAPI🚀](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/)

📝 [Source Code](https://github.com/eriksf/songs-api)
🐞 [Issues](https://github.com/eriksf/songs-api/issues)
"""

logger = logging.getLogger(__name__)


app = FastAPI(
    title="Songs API",
    description=description,
    version="0.1.0",
    docs_url="/",
    root_path=settings.root_path
)

app.include_router(
    songs.router,
    prefix="/v1/songs",
    tags=["songs"]
)

app.include_router(
    status.router,
    prefix="/v1/status",
    tags=["status"]
)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True
    )
