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
from models.entities.stamps import Stamps
from repositories.database.stamps_repository import StampsRepository
from tests.common import MOCK_OBJECT


class TestStampsRepositories(unittest.TestCase):
    """
    Test class for Stamps Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[Stamps(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(Stamps))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_stamps(self, mock_get_session, mock_query, mock_all) -> None:
        response = StampsRepository.get_stamps()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Stamps)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], Stamps)

    if __name__ == '__main__':
        unittest.main()
