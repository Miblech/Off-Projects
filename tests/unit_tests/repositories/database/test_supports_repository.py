"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch

from models.entities.supports import Supports
from repositories.database.supports_repository import SupportsRepository
from tests.common import MOCK_OBJECT
from sqlalchemy.orm import Session, Query

from config import RDS_NODE_MINERVA_RO_NAME
class TestSupportsRepositories(unittest.TestCase):
    """
    Test class for Supports Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[Supports(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(Supports))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_supports(self, mock_get_session, mock_query, mock_all) -> None:
        response = SupportsRepository.get_supports()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Supports)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], Supports)

    if __name__ == '__main__':
        unittest.main()
