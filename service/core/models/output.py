from pydantic import BaseModel, Field


class MessageOutput(BaseModel):
    message: str = Field(..., title="Output message")
    # float_field: float = Field(..., title="A float value")
    # int_field: int = Field(..., title="An integer value")
