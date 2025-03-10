"""
    # Created on October 28, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
import pytest

from models.entities.module_role import ModuleRole
from models.entities.role import Role
from repositories.database.module_role_repository import ModuleRoleRepository
from repositories.database.role_repository import RoleRepository
from repositories.santillana.key_cloak_repository import KeyCloakRepository
from services.authorization_service import AuthorizationService
from exceptions.unauthorized_exception import UnauthorizedException
from tests.common import MOCK_TOKEN_KEYCLOAK, MOCK_ROLE, MOCK_MODULE_ROLE


class TestAuthorizationService(unittest.TestCase):
    """
    Test class for AuthorizationService
    """

    @patch.object(ModuleRoleRepository, "get_module_roles_by_role_ids",
                  return_value=[ModuleRole(**MOCK_MODULE_ROLE)])
    @patch.object(RoleRepository, "get_roles_by_name", return_value=[Role(**MOCK_ROLE)])
    @patch.object(KeyCloakRepository, "check_token", return_value=MOCK_TOKEN_KEYCLOAK)
    def test_authorize_token_keycloak(self, mock_check_token: MagicMock, mock_get_roles_by_name: MagicMock,
                                       mock_get_module_roles_by_role_ids: MagicMock):
        response = AuthorizationService.authorize_token_keycloak("Token", 3)

        mock_check_token.assert_called_once_with("Token")
        mock_get_roles_by_name.assert_called_once_with(MOCK_TOKEN_KEYCLOAK['realm_access']['roles'])
        mock_get_module_roles_by_role_ids.assert_called_once_with([MOCK_ROLE['id']])

        assert response == MOCK_TOKEN_KEYCLOAK

    @patch.object(ModuleRoleRepository, "get_module_roles_by_role_ids",
                  return_value=[ModuleRole(**MOCK_MODULE_ROLE)])
    @patch.object(RoleRepository, "get_roles_by_name", return_value=[Role(**MOCK_ROLE)])
    @patch.object(KeyCloakRepository, "check_token", return_value=MOCK_TOKEN_KEYCLOAK)
    def test_authorize_token_keycloak_not_authorized(self, mock_check_token: MagicMock,
                                                      mock_get_roles_by_name: MagicMock,
                                                      mock_get_module_roles_by_role_ids: MagicMock):
        with pytest.raises(UnauthorizedException):
            AuthorizationService.authorize_token_keycloak("Token", 4)

        mock_check_token.assert_called_once_with("Token")
        mock_get_roles_by_name.assert_called_once_with(MOCK_TOKEN_KEYCLOAK['realm_access']['roles'])
        mock_get_module_roles_by_role_ids.assert_called_once_with([MOCK_ROLE['id']])


if __name__ == "__main__":
    unittest.main()
