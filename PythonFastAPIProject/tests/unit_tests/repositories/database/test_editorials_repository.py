"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch
from models.entities.editorial_area import EditorialArea
from repositories.database.editorials_repository import EditorialsRepository
from tests.common import MOCK_OBJECT
from sqlalchemy.orm import Session, Query

from config import RDS_NODE_MINERVA_RO_NAME
class TestEditorialsRepositories(unittest.TestCase):
    """
    Test class for Editorials Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[EditorialArea(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(EditorialArea))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_editorials(self, mock_get_session, mock_query, mock_all) -> None:
        response = EditorialsRepository.get_editorials()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(EditorialArea)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], EditorialArea)

    if __name__ == '__main__':
        unittest.main()
