"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.analytical_structures_repository import (
    AnalyticalStructuresRepository,
)


class AnalyticalStructuresService(object):
    """
    Class AnalyticalStructuresService
    """

    @staticmethod
    def get_analytical_structures() -> GetObjectsResultResponse:
        """
        Get Analytical Structures
        :Return: GetObjectsResultResponse
        """

        accounts = AnalyticalStructuresRepository.get_analytical_structures()
        return GetObjectsResultResponse.model_validate({"result": {"data": accounts}})
