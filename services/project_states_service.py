"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.project_states_repository import ProjectStatesRepository


class ProjectStatesService(object):
    """
    Class Project States Service
    """

    @staticmethod
    def get_project_states() -> GetObjectsResultResponse:
        """
        Get ProjectStates
        :Return: GetObjectsResultResponse
        """

        result = ProjectStatesRepository.get_project_states()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
