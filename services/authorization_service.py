"""
    # Created on October 25, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from exceptions.unauthorized_exception import UnauthorizedException
from repositories.santillana.key_cloak_repository import KeyCloakRepository
from repositories.database.module_role_repository import ModuleRoleRepository
from repositories.database.role_repository import RoleRepository


class AuthorizationService(object):
    """
    Authorization service
    """

    @staticmethod
    def authorize_token_keycloak(auth_token: str, module_id: int) -> dict:
        """
        :param auth_token: Token of keycloak
        :param module_id: Module ID
        :return: dict
        """

        key_cloak_repository = KeyCloakRepository()
        token_data = key_cloak_repository.check_token(auth_token)

        role_repository = RoleRepository()
        roles = role_repository.get_roles_by_name(token_data["realm_access"]["roles"])

        roles_ids = []

        for role in roles:
            roles_ids.append(role.id)

        module_role_repository = ModuleRoleRepository()
        module_roles = module_role_repository.get_module_roles_by_role_ids(roles_ids)

        for module_role in module_roles:
            if module_id == module_role.module_id:
                return token_data

        raise UnauthorizedException()
