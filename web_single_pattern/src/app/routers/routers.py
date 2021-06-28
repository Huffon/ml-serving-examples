import uuid
from logging import getLogger
from typing import Any, Dict

from fastapi import APIRouter

from src.ml.prediction import Data, translator

logger = getLogger(__name__)
router = APIRouter()


@router.get("/health")
def health() -> Dict[str, str]:
    return {"health": "Ok"}


@router.get("/metadata")
def metadata() -> Dict[str, Any]:
    return {
        "data_type": "string",
        "data_sample": Data().data,
        "prediction_type": "string",
        "prediction_sample": "David Beckham is a former English soccer player.",
    }


@router.get("/predict/test")
def predict_test() -> Dict[str, str]:
    job_id = str(uuid.uuid4())
    translated = translator.translate(data=Data().data)
    logger.info(f"Test {job_id}")
    return {"prediction": translated}


@router.post("/predict")
def predict(data: Data) -> Dict[str, str]:
    job_id = str(uuid.uuid4())
    translated = translator.translate(data.data)
    logger.info(f"{job_id}")
    return {"prediction": translated}
