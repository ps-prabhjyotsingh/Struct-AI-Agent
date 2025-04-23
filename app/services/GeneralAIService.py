from pydantic_ai import Agent, models

from app.common.Singleton import Singleton
from app.interfaces.AIService import AIService


class GeneralAIService(AIService, metaclass=Singleton):

    #defaultModel = "anthropic:claude-3-5-haiku-latest"
    defaultModel = "openai:gpt-4o"

    def __init__(self, model: models.KnownModelName):
        self.model = model
        #super().__init__()//intentionally skipped

    def becomeSomeone(self):
        #self.system_prompts.append("A system prompt to define the personality of the AI.")
        pass
