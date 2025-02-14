"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
from services.purposes_service import PurposesService
from tests.common import MOCK_OBJECTS, MOCK_OBJECT


class TestPurposesService(unittest.TestCase):

    def setUp(self) -> None:
        patch.stopall()
        return super().setUp()

    @patch('repositories.database.purposes_repository.PurposesRepository.get_purposes', return_value=MOCK_OBJECTS)
    def test_get_purposes(self, mock_get_courses: MagicMock) -> None:
        service = PurposesService()
        response = service.get_purposes()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

if __name__ == '__main__':
    unittest.main()