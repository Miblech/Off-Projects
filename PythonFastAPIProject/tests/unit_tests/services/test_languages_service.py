"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
from services.languages_service import LanguagesService
from tests.common import MOCK_OBJECTS, MOCK_OBJECT


class TestLanguagesService(unittest.TestCase):

    def setUp(self) -> None:
        patch.stopall()
        return super().setUp()

    @patch('repositories.database.languages_repository.LanguagesRepository.get_languages', return_value=MOCK_OBJECTS)
    def test_get_languages(self, mock_get_courses: MagicMock) -> None:
        service = LanguagesService()
        response = service.get_languages()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

if __name__ == '__main__':
    unittest.main()