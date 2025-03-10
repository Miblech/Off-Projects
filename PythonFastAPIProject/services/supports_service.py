"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.supports_repository import SupportsRepository


class SupportsService(object):
    """
    Class  Support Service
    """

    @staticmethod
    def get_support() -> GetObjectsResultResponse:
        """
        Get Support
        :Return: GetObjectsResultResponse
        """

        result = SupportsRepository.get_supports()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
