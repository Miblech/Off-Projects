"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

# Libraries dependencies
from http import HTTPStatus

from fastapi import HTTPException
from pydantic import BaseModel

from config import CODE_RESPONSE_ERROR, RESPONSE_UNAUTHORIZED_EXCEPTION


class UnauthorizedExceptionModel(BaseModel):
    """
    Unauthorized exception for documenting purposes
    """

    code: int = CODE_RESPONSE_ERROR
    message: str = RESPONSE_UNAUTHORIZED_EXCEPTION


class UnauthorizedException(HTTPException):
    """
    Unauthorized exception class reference.

    Represents a 401 Unauthorized HTTP Error
    this status code is raised when the user fails the authentication process
    """

    status_code = HTTPStatus.UNAUTHORIZED.value

    def __init__(self):
        super().__init__(
            status_code=HTTPStatus.UNAUTHORIZED.value,
            detail=UnauthorizedExceptionModel().model_dump(),
        )
