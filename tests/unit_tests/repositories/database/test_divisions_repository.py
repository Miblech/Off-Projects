"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch
from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.divisions import Divisions
from repositories.database.divisions_repository import DivisionRepository
from tests.common import MOCK_OBJECT
from sqlalchemy.orm import Session, Query

class TestDivisionsRepositories(unittest.TestCase):
    """
    Test class for Divisions Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[Divisions(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(Divisions))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_divisions(self, mock_get_session, mock_query, mock_all) -> None:
        response = DivisionRepository.get_division()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Divisions)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], Divisions)

    if __name__ == '__main__':
        unittest.main()
