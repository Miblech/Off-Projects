"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from pydantic import BaseModel, ConfigDict

from models.responses.standart_response import StandardResponse


class GetObjectResponse(BaseModel):
    """
    Response DTO for GET Object
    """

    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class GetObjectDataResponse(BaseModel):
    """
    Result DTO for Specific Object
    """

    data: GetObjectResponse


class GetObjectResultResponse(StandardResponse):
    result: GetObjectDataResponse | None = None
