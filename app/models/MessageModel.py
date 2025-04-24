import datetime

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.dialects.mysql import TEXT



class MessageModel(SQLModel, table=True):
    ENTITY_AI: int = 1
    ENTITY_USER: int = 2
    STATUS_SUCCESS: int = 1
    STATUS_ERROR: int = 0

    id: int = Field(primary_key=True)
    message: str = Field(sa_column=Column(TEXT), max_length=65000)
    conversation_id: int = Field(foreign_key="conversationmodel.id")
    entity: int #0 - User, 1 - AI
    request_tokens:  int | None
    response_tokens: int | None
    status: int = Field(default=0) #1 - OK, 0 - error
    error: str|None = Field(default=None)
    time: int|None = Field(default=int(datetime.datetime.now(datetime.UTC).timestamp()))
    conversation: "ConversationModel" = Relationship(back_populates="messages")
