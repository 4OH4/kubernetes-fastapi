from fastapi import APIRouter

from service.core.models.output import MessageOutput
from service.core.models.input import MessageInput
from service.core.logic.business_logic import my_function

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

    return {"message": "Hello, world!"}
