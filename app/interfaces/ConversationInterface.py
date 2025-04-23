from pydantic import BaseModel


class Conversation(BaseModel):
    message: str
    referencedBy: str
