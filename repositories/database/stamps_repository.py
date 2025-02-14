"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.stamps import Stamps

from repositories.database.manager.database_factory import db_manager

CLASS = "Stamps Repository"


class StampsRepository(object):
    """
    Stamps Repository class
    """

    @staticmethod
    def get_stamps() -> list[Stamps]:
        """
        Get List of Stamps

        :return: List of Stamps
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Stamps).all()
