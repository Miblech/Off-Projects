"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock

from config import RDS_NODE_RO_NAME
from models.entities.module_role import ModuleRole
from tests.common import MOCK_MODULE_ROLE
from repositories.database.module_role_repository import ModuleRoleRepository

class TestModuleRoleRepository(unittest.TestCase):
    """
    Test class for ModuleRoleRepository
    """
    @patch("repositories.database.module_role_repository.db_manager")
    def test_get_roles_by_name(self, mock_db_manager: MagicMock) -> None:
        # Mock session and query behavior
        mock_session = MagicMock()
        mock_db_manager.get_session.return_value = mock_session

        mock_query = mock_session.query.return_value
        mock_filter = mock_query.filter.return_value
        mock_filter.all.return_value = [ModuleRole(**MOCK_MODULE_ROLE)]

        # Call the method
        result = ModuleRoleRepository.get_module_roles_by_role_ids([1])

        # Assertions
        mock_db_manager.get_session.assert_called_once_with(RDS_NODE_RO_NAME)
        mock_session.query.assert_called_once_with(ModuleRole)
        mock_query.filter.assert_called_once()
        mock_filter.all.assert_called_once()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], ModuleRole)
        self.assertEqual(result[0].role_id, MOCK_MODULE_ROLE["role_id"])


if __name__ == "__main__":
    unittest.main()