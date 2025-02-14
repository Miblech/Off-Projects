"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from fastapi import HTTPException
from pydantic import BaseModel

from config import CODE_RESPONSE_ERROR, RESPONSE_INTERNAL_SERVER_EXCEPTION


class InternalServerExceptionModel(BaseModel):
    """
    Internal Server Exception for documenting purposes
    """

    code: int = CODE_RESPONSE_ERROR
    message: str = RESPONSE_INTERNAL_SERVER_EXCEPTION


class InternalServerException(HTTPException):
    """
    Internal Server Exception to raise to the final user
    """

    status_code: int = 500

    def __init__(self) -> None:
        super().__init__(
            status_code=self.status_code,
            detail=InternalServerExceptionModel().model_dump(),
        )
