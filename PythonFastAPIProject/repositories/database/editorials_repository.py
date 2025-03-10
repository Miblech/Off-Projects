"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.editorial_area import EditorialArea

from repositories.database.manager.database_factory import db_manager

CLASS = "Editorials Repository"


class EditorialsRepository(object):
    """
    Editorials Repository
    """

    @staticmethod
    def get_editorials() -> list[EditorialArea]:
        """
        Get Editorials

        :return: List of Editorials
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(EditorialArea).all()
