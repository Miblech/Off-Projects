"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.structure_types_repository import StructureTypesRepository


class StructureTypesService(object):
    """
    Class Structure Types Service
    """

    @staticmethod
    def get_structure_types() -> GetObjectsResultResponse:
        """
        Get Structure Types
        :Return: GetObjectsResultResponse
        """

        result = StructureTypesRepository.get_structure_types()
        return GetObjectsResultResponse.model_validate({"result": {"data": result}})
