"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.editorials_repository import EditorialsRepository


class EditorialsService(object):
    """
    Class Editorials Service
    """

    @staticmethod
    def get_editorials() -> GetObjectsResultResponse:
        """
        Get Editorials
        :Return: GetObjectsResultResponse
        """

        result = EditorialsRepository.get_editorials()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
