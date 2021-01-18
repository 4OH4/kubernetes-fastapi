from pydantic import BaseModel, Field


class MessageOutput(BaseModel):
    message1: str = Field(..., title="Greeting")
    message2: str = Field(..., title="Calculation result")
    n: int = Field(..., title="n: a large integer")
    largest_prime_factor: int = Field(..., title="Largest prime factor of n")
    elapsed_time: float = Field(..., title="Calculation time (seconds)")
