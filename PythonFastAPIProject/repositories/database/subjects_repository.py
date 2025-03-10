"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.subjects import Subjects

from repositories.database.manager.database_factory import db_manager

CLASS = "Subjects Repository"


class SubjectsRepository(object):
    """
    Subjects Class Repository
    """

    @staticmethod
    def get_subjects() -> list[Subjects]:
        """
        Get list of subjects.

        :return: list of Subjects
        """
        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Subjects).all()
