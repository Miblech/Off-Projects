"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.languages_repository import LanguagesRepository


class LanguagesService:
    """
    Class LanguagesService
    """

    @staticmethod
    def get_languages() -> GetObjectsResultResponse:
        """
        Get Languages
        :Return: LanguagesResponse
        """

        languages = LanguagesRepository.get_languages()
        return GetObjectsResultResponse.model_validate({"result": {"data": languages}})
