"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.purposes import Purposes

from repositories.database.manager.database_factory import db_manager

CLASS = "Purposes Repository"


class PurposesRepository(object):
    """
    Project Purposes
    """

    @staticmethod
    def get_purposes() -> list[Purposes]:
        """
        Get Purposes

        :return: List of Purposes
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Purposes).all()
