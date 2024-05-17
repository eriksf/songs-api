import logging

from fastapi import APIRouter

from app.config import settings
from app.routers.status.models import Status

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("", response_model=Status)
async def get_status():
    return {
        "name": settings.project_name,
        "version": settings.project_version,
        "database_server": settings.db_server,
        "database_port": settings.db_port,
        "database_name": settings.db_name
    }
