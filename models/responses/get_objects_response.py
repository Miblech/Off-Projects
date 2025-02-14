"""
    # Created on October 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from pydantic import BaseModel

from config import CODE_RESPONSE_NONE
from models.responses.get_object_response import GetObjectResponse


class GetObjectsDataResponse(BaseModel):
    """
    Class GetDataResponse

    data : [modules]
    """

    data: list[GetObjectResponse]


class GetObjectsResultResponse(BaseModel):
    """
    Class GetResultsResponse

    :return result:
                data: list[modules]
    """

    result: GetObjectsDataResponse
    code: int = CODE_RESPONSE_NONE
    message: str = ""
