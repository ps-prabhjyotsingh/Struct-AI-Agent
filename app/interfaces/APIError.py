from pydantic import BaseModel


class APIError(BaseModel):
    status: str = "error"
    message: str