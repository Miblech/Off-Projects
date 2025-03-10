"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from http import HTTPStatus

from fastapi import HTTPException
from pydantic import BaseModel

from config import VALIDATION_EXCEPTION_DETAIL, CODE_RESPONSE_NONE


class ValidationDetailsModel(BaseModel):
    loc: list[str] | tuple
    msg: str
    type: str
    ctx: dict | None = None


class ValidationExceptionModel(BaseModel):
    """
    Pydantic Validation Exception for documenting purposes
    """

    code: int = CODE_RESPONSE_NONE
    message: str = VALIDATION_EXCEPTION_DETAIL
    errors: list[ValidationDetailsModel]


class ValidationException(HTTPException):
    """
    Pydantic Validation Exception to raise to the final user
    """

    status_code: int = HTTPStatus.UNPROCESSABLE_ENTITY.value

    def __init__(self, errors: list[ValidationDetailsModel]) -> None:
        super().__init__(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY.value,
            detail=ValidationExceptionModel(errors=errors).model_dump(),
        )
