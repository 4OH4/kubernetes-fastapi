from pydantic import BaseModel, Field


class MessageInput(BaseModel):
    pass
    # field1: str = Field(..., title="First string field")
    # field2: str = Field(..., title="Second string field")
