from pydantic_ai import models, Agent


class AIService:
    model: models.KnownModelName
    key: str
    agent: Agent[None, str]

    def __init__(self):
        raise NotImplementedError
    @classmethod
    def getInstance(cls, model: models.KnownModelName, key: str):
        return cls.__call__(model, key)

    def query(self, prompt: str):
        self.agent = Agent(
            self.model
        )
        result = self.agent.run_sync(prompt)
        print(result)
        return result