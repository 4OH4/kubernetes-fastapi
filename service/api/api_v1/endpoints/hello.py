from fastapi import APIRouter

from service.core.models.output import MessageOutput
from service.core.models.input import MessageInput
from service.core.logic.business_logic import run_prime_factor_calculation

router = APIRouter()


# @router.get("/example", tags=["example get"])
# def example_get():
#     """
#     Say hej!

#     This will greet you properly

#     And this path operation will:
#     * return "hej!"
#     """
#     return {"msg": "Hej!"}


@router.post("/hello", response_model=MessageOutput, tags=["hello post"])
def hello_endpoint(inputs: MessageInput):
    """
    Respond to requests on the hello endpoint

    """

    n, largest_prime_factor, elapsed_time = run_prime_factor_calculation()

    return {
        "message1": "Hello, world!",
        "message2": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }
