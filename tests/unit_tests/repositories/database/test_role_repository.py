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
from models.entities.role import Role
from repositories.database.role_repository import RoleRepository

class TestRoleRepository(unittest.TestCase):
    """
    Test class for RoleRepository
    """

    def setUp(self) -> None:
        self.mock_read_session = MagicMock()
        self.mock_role = Role(id=1, name="admin_flujo_editorial")

    @patch("repositories.database.role_repository.db_manager")
    def test_get_roles_by_name(self, mock_db_manager: MagicMock) -> None:
        # Mock the read session
        mock_db_manager.get_session.return_value = self.mock_read_session

        # Configure the mock to return the expected result
        mock_query = self.mock_read_session.query.return_value
        mock_filter = mock_query.filter.return_value
        mock_filter.all.return_value = [self.mock_role]

        # Call the method
        result = RoleRepository.get_roles_by_name(["admin_flujo_editorial"])

        # Assertions
        mock_db_manager.get_session.assert_called_once_with(RDS_NODE_RO_NAME)
        self.mock_read_session.query.assert_called_once_with(Role)
        mock_query.filter.assert_called_once()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, self.mock_role.name)

if __name__ == "__main__":
    unittest.main()
