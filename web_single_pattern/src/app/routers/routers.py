import uuid
from logging import getLogger
from typing import Dict

from fastapi import APIRouter

logger = getLogger(__name__)
router = APIRouter()


@router.get("/health")
def health() -> Dict[str, str]:
    return {"health": "Ok"}


@router.post("/predict")
def predict(data):
    job_id = str(uuid.uuid4())
    logger.info(f"{job_id}")
    return {"prediction": "N/A"}
