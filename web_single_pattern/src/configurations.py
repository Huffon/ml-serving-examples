import os
from logging import getLogger

logger = getLogger(__name__)


class ApiConfigurations:
    title = os.getenv("API_TITLE", "ServingPattern")
    description = os.getenv("API_DESCRIPTION", "Web Single Pattern")
    version = os.getenv("API_VERSION", "0.1")


logger.info(f"{ApiConfigurations.__name__}: {ApiConfigurations.__dict__}")
