"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.analytical_structures import AnalyticalStructures
from repositories.database.manager.database_factory import db_manager

CLASS = "Analytical Structures Repository"


class AnalyticalStructuresRepository(object):
    """
    Analytical Structures Repository
    """

    @staticmethod
    def get_analytical_structures() -> list[AnalyticalStructures]:
        """
        Get Analytical Accounts

        :return: List of Analytical Accounts
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(AnalyticalStructures).all()
