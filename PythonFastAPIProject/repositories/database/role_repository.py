"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_RO_NAME, RDS_NODE_RW_NAME
from models.entities.role import Role
from repositories.database.manager.database_factory import db_manager


class RoleRepository(object):
    """
    Class RoleRepository
    """

    @staticmethod
    def get_roles_by_name(role_names: list[str]) -> list[Role]:
        """
        Get Roles
        :param [str] role_names
        :return: Roles
        :rtype: [Type[Role]]
        """
        session = db_manager.get_session(RDS_NODE_RO_NAME)
        roles = session.query(Role).filter(Role.name.in_(role_names)).all()
        return roles

    @staticmethod
    def write_roles_by_name(role_names: list[str]) -> list[Role]:
        """
        Get Roles
        :param [str] role_names
        :return: Roles
        :rtype: [Type[Role]]
        """
        session = db_manager.get_session(RDS_NODE_RW_NAME)
        roles = session.query(Role).filter(Role.name.in_(role_names)).all()
        return roles
