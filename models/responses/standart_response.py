"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from datetime import datetime
from pydantic import BaseModel


class StandardResponse(BaseModel):
    """
    Class StandardResponse
    """

    code: int = 0
    message: str = ""
    result: object


def validator_datetime(v):
    if isinstance(v, datetime):
        return v.strftime("%Y-%m-%d %H:%M:%S")
    return v
