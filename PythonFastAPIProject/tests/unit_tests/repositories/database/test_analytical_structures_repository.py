"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch
from sqlalchemy.orm import Session, Query
from config import RDS_NODE_MINERVA_RO_NAME
from models.entities.analytical_structures import AnalyticalStructures
from repositories.database.analytical_structures_repository import AnalyticalStructuresRepository
from tests.common import MOCK_OBJECT


class TestAnalyticalStructuresRepositories(unittest.TestCase):
    """
    Test class for Analytical Structures Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[AnalyticalStructures(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(AnalyticalStructures))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_analytical_structures(self, mock_get_session, mock_query, mock_all) -> None:
        response = AnalyticalStructuresRepository.get_analytical_structures()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(AnalyticalStructures)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], AnalyticalStructures)

    if __name__ == '__main__':
        unittest.main()
