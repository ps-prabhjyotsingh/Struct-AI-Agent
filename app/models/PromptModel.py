from sqlalchemy import Column
from sqlmodel import SQLModel, Field
from sqlalchemy.dialects.mysql import TEXT,LONGTEXT

class PromptModel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    prompt: str = Field(sa_column=Column(TEXT), max_length=65000)
    referenced_by: str = Field(max_length=255)
    request_tokens:  int | None
    response_tokens: int | None
    response: str|None = Field(default=None,sa_column=Column(LONGTEXT))