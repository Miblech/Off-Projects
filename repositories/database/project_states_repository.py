"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.project_states import ProjectStates

from repositories.database.manager.database_factory import db_manager

CLASS = "Project States Repository"


class ProjectStatesRepository(object):
    """
    Project States Repository
    """

    @staticmethod
    def get_project_states() -> list[ProjectStates]:
        """
        Get Project States

        :return: List of Project States
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(ProjectStates).all()
