"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
from services.courses_service import CourseService
from tests.common import MOCK_OBJECTS, MOCK_OBJECT


class TestCoursesService(unittest.TestCase):

    def setUp(self) -> None:
        patch.stopall()
        return super().setUp()

    @patch('repositories.database.courses_repository.CoursesRepository.get_courses', return_value=MOCK_OBJECTS)
    def test_get_courses(self, mock_get_courses: MagicMock) -> None:
        course_service = CourseService()
        response = course_service.get_courses()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

if __name__ == '__main__':
    unittest.main()