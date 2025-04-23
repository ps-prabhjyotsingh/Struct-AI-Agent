from pydantic import BaseModel


class ConversationReplyType(BaseModel):
    message: str
