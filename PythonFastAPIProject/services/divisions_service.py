"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.divisions_repository import DivisionRepository


class DivisionsService(object):
    """
    Class Divisions Service
    """

    @staticmethod
    def get_division() -> GetObjectsResultResponse:
        """
        Get Division
        :Return: GetObjectsResultResponse
        """

        result = DivisionRepository.get_division()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
