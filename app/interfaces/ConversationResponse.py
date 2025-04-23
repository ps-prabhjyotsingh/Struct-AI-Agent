from app.interfaces.ConversationBase import ConversationBase
from app.models.MessageModel import MessageModel


class ConversationResponse(ConversationBase):
    messages: list[MessageModel]
