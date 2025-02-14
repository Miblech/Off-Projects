"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch

from models.entities.structure_types import StructureTypes
from repositories.database.structure_types_repository import StructureTypesRepository
from tests.common import MOCK_OBJECT
from sqlalchemy.orm import Session, Query

from config import RDS_NODE_MINERVA_RO_NAME
class TestStructuresTypesRepositories(unittest.TestCase):
    """
    Test class for Structures Types Repositories
    """

    @patch('sqlalchemy.orm.Query.all', return_value=[StructureTypes(**MOCK_OBJECT)])
    @patch('sqlalchemy.orm.Session.query', return_value=Query(StructureTypes))
    @patch('repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session',
           return_value=Session())
    def test_get_structure_types(self, mock_get_session, mock_query, mock_all) -> None:
        response = StructureTypesRepository.get_structure_types()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(StructureTypes)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT['id']
        assert response[0].name == MOCK_OBJECT['name']
        assert isinstance(response[0], StructureTypes)

    if __name__ == '__main__':
        unittest.main()
