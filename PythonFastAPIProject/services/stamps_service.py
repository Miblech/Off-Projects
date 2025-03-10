"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.stamps_repository import StampsRepository


class StampsService(object):
    """
    Class StampsService
    """

    @staticmethod
    def get_stamps() -> GetObjectsResultResponse:
        """
        Get Stamps
        :Return: StampsResponse
        """

        stamps = StampsRepository.get_stamps()
        return GetObjectsResultResponse.model_validate({"result": {"data": stamps}})
