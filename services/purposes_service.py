"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.purposes_repository import PurposesRepository


class PurposesService(object):
    """
    Class Purposes Service
    """

    @staticmethod
    def get_purposes() -> GetObjectsResultResponse:
        """
        Get Purposes
        :Return: GetObjectsResultResponse
        """

        result = PurposesRepository.get_purposes()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
