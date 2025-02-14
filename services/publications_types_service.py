"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.publications_types_repository import (
    PublicationsTypesRepository,
)


class PublicationsService(object):
    """
    Class Publications Service
    """

    @staticmethod
    def get_publications_types() -> GetObjectsResultResponse:
        """
        Get Publications
        :Return: GetObjectsResultResponse
        """

        result = PublicationsTypesRepository.get_publications_types()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
