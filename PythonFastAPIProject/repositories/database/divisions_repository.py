"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.divisions import Divisions

from repositories.database.manager.database_factory import db_manager

CLASS = "Division Repository"


class DivisionRepository(object):
    """
    Division Repository
    """

    @staticmethod
    def get_division() -> list[Divisions]:
        """
        Get Division

        :return: List of Division

        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Divisions).all()
