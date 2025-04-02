from pydantic_ai import Agent, models

from app.common.Singleton import Singleton
from app.interfaces.AIService import AIService


class GeneralAIService(AIService, metaclass=Singleton):

    def __init__(self, model: models.KnownModelName, key: str):
        self.model = model
        self.key = key
        #super().__init__()//intentionally skipped
