"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.publication_type import PublicationType

from repositories.database.manager.database_factory import db_manager

CLASS = "Publications Types Repository"


class PublicationsTypesRepository(object):
    """
    Project Publications Types
    """

    @staticmethod
    def get_publications_types() -> list[PublicationType]:
        """
        Get Publications

        :return: List of Publications
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(PublicationType).all()
