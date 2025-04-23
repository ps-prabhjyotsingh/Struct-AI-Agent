from sqlalchemy import Column
from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.mysql import BLOB
import datetime

class ConversationBase(SQLModel):
    id: int = Field(primary_key=True)
    referenced_by: str = Field(max_length=255)
    start_time: int | None = Field(default=int(datetime.datetime.now(datetime.UTC).timestamp()))
    all_messages: str = Field(sa_column=Column(BLOB))
    new_messages: str = Field(sa_column=Column(BLOB))
