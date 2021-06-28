import uuid
from logging import getLogger
from typing import Dict

from fastapi import APIRouter

from src.ml.prediction import Data, translator

logger = getLogger(__name__)
router = APIRouter()


@router.get("/health")
def health() -> Dict[str, str]:
    return {"health": "Ok"}


@router.get("/predict/test")
def predict_test():
    job_id = str(uuid.uuid4())
    translated = translator.predict(data=Data().data)
    logger.info(f"Test {job_id}")
    return {"prediction": translated}


@router.post("/predict")
def predict(data: Data):
    job_id = str(uuid.uuid4())
    translated = translator.predict(data.data)
    logger.info(f"{job_id}")
    return {"prediction": translated}
