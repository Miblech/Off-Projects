"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.subjects_repository import SubjectsRepository


class SubjectsService(object):
    """
    Class SubjectsService
    """

    @staticmethod
    def get_subjects() -> GetObjectsResultResponse:
        """
        Get Subjects
        :Return: SubjectsResponse
        """

        subjects = SubjectsRepository.get_subjects()
        return GetObjectsResultResponse.model_validate({"result": {"data": subjects}})
