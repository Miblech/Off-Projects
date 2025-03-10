"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.project_types_repository import ProjectTypesRepository


class ProjectTypesService(object):
    """
    Class Project Types Service
    """

    @staticmethod
    def get_project_types() -> GetObjectsResultResponse:
        """
        Get ProjectTypes
        :Return: GetObjectsResultResponse
        """

        result = ProjectTypesRepository.get_project_types()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
