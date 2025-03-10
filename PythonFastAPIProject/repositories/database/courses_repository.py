"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.courses import Courses
from repositories.database.manager.database_factory import db_manager

CLASS = "Courses Repository"


class CoursesRepository(object):
    """
    Courses Repository
    """

    @staticmethod
    def get_courses() -> list[Courses]:
        """
        Get courses

        :return: List of courses
        """
        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(Courses).all()
