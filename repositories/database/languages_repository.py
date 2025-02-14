"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.languages import Languages

from repositories.database.manager.database_factory import db_manager

CLASS = "Languages Repository"


class LanguagesRepository(object):
    """
    Languages Repository class
    """

    @staticmethod
    def get_languages() -> list[Languages]:
        """
        Get Languages List

        :return: List of Languages
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Languages).all()
