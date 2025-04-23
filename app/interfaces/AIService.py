from pydantic_ai import models, Agent
from typing import Self

class AIService:
    model: models.KnownModelName
    agent: Agent[None, str] = Agent()
    defaultModel: models.KnownModelName | None = None
    system_prompts: list[str] = []

    def __init__(self):
        raise NotImplementedError
    @classmethod
    def getInstance(cls, model: models.KnownModelName = None) -> Self:
        if(model is None and cls.defaultModel is None):
            raise NotImplementedError
        elif(model is None and cls.defaultModel != None):
            model = cls.defaultModel

        return cls.__call__(model)


    def query(self, prompt: str, history: bytes|None = None):
        self.agent = Agent(
            self.model
        )
        print("Calling AI with Prompt")
        print(prompt)
        result = self.agent.run_sync(prompt, message_history=history)
        return result

    @agent.system_prompt
    def add_system_prompt(self):
        global agent
        system_prompt = ""
        for prompt in self.system_prompts:
            system_prompt += prompt+"\n"
        print("System prompt is "+ system_prompt)
        return system_prompt