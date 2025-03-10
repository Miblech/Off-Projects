"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock

from services.analytical_accounts_service import AnalyticalAccountsService
from services.analytical_structures_service import AnalyticalStructuresService
from services.courses_service import CourseService
from services.divisions_service import DivisionsService
from services.editorials_service import EditorialsService
from services.languages_service import LanguagesService
from services.project_states_service import ProjectStatesService
from services.project_types_service import ProjectTypesService
from services.publications_types_service import PublicationsService
from services.purposes_service import PurposesService
from services.stamps_service import StampsService
from services.structure_types_service import StructureTypesService
from services.subjects_service import SubjectsService
from services.supports_service import SupportsService
from services.third_party_departments_service import ThirdPartyDepartmentsService
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

    @patch('repositories.database.languages_repository.LanguagesRepository.get_languages', return_value=MOCK_OBJECTS)
    def test_get_languages(self, mock_get_courses: MagicMock) -> None:
        service = LanguagesService()
        response = service.get_languages()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.stamps_repository.StampsRepository.get_stamps', return_value=MOCK_OBJECTS)
    def test_get_stamps(self, mock_get_courses: MagicMock) -> None:
        service = StampsService()
        response = service.get_stamps()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.subjects_repository.SubjectsRepository.get_subjects', return_value=MOCK_OBJECTS)
    def test_get_subjects(self, mock_get_courses: MagicMock) -> None:
        service = SubjectsService()
        response = service.get_subjects()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.analytical_accounts_repository.AnalyticalAccountsRepository.get_analytical_accounts',
           return_value=MOCK_OBJECTS)
    def test_get_analytical_accounts(self, mock_get_courses: MagicMock) -> None:
        service = AnalyticalAccountsService()
        response = service.get_analytical_accounts()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch(
        'repositories.database.analytical_structures_repository.AnalyticalStructuresRepository.get_analytical_structures',
        return_value=MOCK_OBJECTS)
    def test_get_analytical_structures(self, mock_get_courses: MagicMock) -> None:
        service = AnalyticalStructuresService()
        response = service.get_analytical_structures()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.divisions_repository.DivisionRepository.get_division', return_value=MOCK_OBJECTS)
    def test_get_divisions(self, mock_get_courses: MagicMock) -> None:
        service = DivisionsService()
        response = service.get_division()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.editorials_repository.EditorialsRepository.get_editorials', return_value=MOCK_OBJECTS)
    def test_get_editorials(self, mock_get_courses: MagicMock) -> None:
        service = EditorialsService()
        response = service.get_editorials()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.project_states_repository.ProjectStatesRepository.get_project_states',
           return_value=MOCK_OBJECTS)
    def test_get_project_states(self, mock_get_courses: MagicMock) -> None:
        service = ProjectStatesService()
        response = service.get_project_states()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.project_types_repository.ProjectTypesRepository.get_project_types',
           return_value=MOCK_OBJECTS)
    def test_get_project_types(self, mock_get_courses: MagicMock) -> None:
        service = ProjectTypesService()
        response = service.get_project_types()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.publications_types_repository.PublicationsTypesRepository.get_publications_types',
           return_value=MOCK_OBJECTS)
    def test_get_publications_types(self, mock_get_courses: MagicMock) -> None:
        service = PublicationsService()
        response = service.get_publications_types()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.purposes_repository.PurposesRepository.get_purposes', return_value=MOCK_OBJECTS)
    def test_get_purposes(self, mock_get_courses: MagicMock) -> None:
        service = PurposesService()
        response = service.get_purposes()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.structure_types_repository.StructureTypesRepository.get_structure_types',
           return_value=MOCK_OBJECTS)
    def test_get_structure_types(self, mock_get_courses: MagicMock) -> None:
        service = StructureTypesService()
        response = service.get_structure_types()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch('repositories.database.supports_repository.SupportsRepository.get_supports', return_value=MOCK_OBJECTS)
    def test_get_supports(self, mock_get_courses: MagicMock) -> None:
        service = SupportsService()
        response = service.get_support()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']

    @patch(
        'repositories.database.third_party_departments_repository.ThirdPartyDepartmentsRepository.get_third_party_departments',
        return_value=MOCK_OBJECTS)
    def test_get_third_party_departments(self, mock_get_courses: MagicMock) -> None:
        service = ThirdPartyDepartmentsService()
        response = service.get_third_party_departments()
        mock_get_courses.assert_called_once()

        assert response.result.data[0].id == MOCK_OBJECT['id']
        assert response.result.data[0].name == MOCK_OBJECT['name']


if __name__ == '__main__':
    unittest.main()
