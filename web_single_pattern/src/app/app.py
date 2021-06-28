from logging import getLogger

from fastapi import FastAPI

from src.app.routers import routers
from src.configurations import ApiConfigurations

logger = getLogger(__name__)

app = FastAPI(
    title=ApiConfigurations.title,
    description=ApiConfigurations.description,
    version=ApiConfigurations.version,
)

app.include_router(routers.router, prefix="", tags=[""])
