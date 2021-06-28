import os
from logging import getLogger

logger = getLogger(__name__)


class ApiConfigurations:
    title = os.getenv("API_TITLE", "ServingPattern")
    description = os.getenv("API_DESCRIPTION", "Web Single Pattern")
    version = os.getenv("API_VERSION", "0.1")


class ModelConfigurations:
    model_name = os.getenv("MODEL_NAME", "Helsinki-NLP/opus-mt-ko-en")


logger.info(f"{ApiConfigurations.__name__}: {ApiConfigurations.__dict__}")
logger.info(f"{ModelConfigurations.__name__}: {ModelConfigurations.__dict__}")
