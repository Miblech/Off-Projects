"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.structure_types import StructureTypes

from repositories.database.manager.database_factory import db_manager

CLASS = "Structure Types Repository"


class StructureTypesRepository(object):
    """
    Project StructureTypes
    """

    @staticmethod
    def get_structure_types() -> list[StructureTypes]:
        """
        Get Structure Types

        :return: List of Structure Types
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(StructureTypes).all()
