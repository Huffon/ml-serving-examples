from logging import getLogger

from pydantic import BaseModel
from transformers import pipeline

from src.configurations import ModelConfigurations

logger = getLogger(__name__)


class Data(BaseModel):
    data: str = "데이비드 베컴은 잉글랜드의 전 축구 선수이다."


class Translator(object):

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.translator = None
        self.load_model()

    def load_model(self):
        logger.info(f"Load model: {self.model_name}")
        self.translator = pipeline(
            task="text2text-generation",
            model=self.model_name,
        )
        logger.info("Initialized model")

    def predict(self, data: str):
        translated = self.translator(data)
        return translated


translator = Translator(model_name=ModelConfigurations().model_name)
