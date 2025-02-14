"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
from services.publications_types_service import PublicationsService
from tests.common import MOCK_OBJECTS, MOCK_OBJECT


class TestPublicationTypesService(unittest.TestCase):

    def setUp(self) -> None:
        patch.stopall()
        return super().setUp()

    @patch('repositories.database.publications_types_repository.PublicationsTypesRepository.get_publications_types',
           return_value=MOCK_OBJECTS)
    def test_get_publications_types(self, mock_get_courses: MagicMock) -> None:
        service = PublicationsService()
        response = service.get_publications_types()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

if __name__ == '__main__':
    unittest.main()