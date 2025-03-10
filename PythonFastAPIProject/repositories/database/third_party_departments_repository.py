"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from typing import List

from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.third_party_departments import ThirdPartyDepartments

from repositories.database.manager.database_factory import db_manager

CLASS = "Structure Types Repository"


class ThirdPartyDepartmentsRepository(object):
    """
    Project ThirdPartyDepartments
    """

    @staticmethod
    def get_third_party_departments() -> List[ThirdPartyDepartments]:
        """
        Get ThirdPartyDepartments

        :return: List of ThirdPartyDepartments
        """

        session = db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
        return session.query(ThirdPartyDepartments).all()
