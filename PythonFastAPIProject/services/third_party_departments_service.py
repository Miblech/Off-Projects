"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.third_party_departments_repository import (
    ThirdPartyDepartmentsRepository,
)


class ThirdPartyDepartmentsService(object):
    """
    Class  Third Party Departments Service
    """

    @staticmethod
    def get_third_party_departments() -> GetObjectsResultResponse:
        """
        Get Third Party Departments
        :Return: GetObjectsResultResponse
        """

        result = ThirdPartyDepartmentsRepository.get_third_party_departments()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
