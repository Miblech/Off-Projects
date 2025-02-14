"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from config import RDS_NODE_RO_NAME
from models.entities.module_role import ModuleRole
from repositories.database.manager.database_factory import db_manager


class ModuleRoleRepository(object):
    """
    Class ModuleRoleRepository
    """

    @staticmethod
    def get_module_roles_by_role_ids(role_ids: list[int | None]) -> list[ModuleRole]:
        """
        Get Module Roles
        :param [int] role_ids
        :return: Module Roles
        :rtype: [Type[ModuleRole]]
        """
        session = db_manager.get_session(RDS_NODE_RO_NAME)
        return (
            session.query(ModuleRole)
            .filter(ModuleRole.role_id.in_(role_ids), ModuleRole.active.is_(True))
            .all()
        )
