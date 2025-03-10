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
from models.entities.courses import Courses
from models.entities.languages import Languages
from models.entities.stamps import Stamps
from models.entities.subjects import Subjects
from models.entities.analytical_structures import AnalyticalStructures
from models.entities.analytical_accounts import AnalyticalAccounts
from models.entities.divisions import Divisions
from models.entities.editorial_area import EditorialArea
from models.entities.project_states import ProjectStates
from models.entities.project_types import ProjectTypes
from models.entities.publication_type import PublicationType
from models.entities.purposes import Purposes
from models.entities.structure_types import StructureTypes
from models.entities.supports import Supports
from models.entities.third_party_departments import ThirdPartyDepartments
from repositories.database.analytical_accounts_repository import (
    AnalyticalAccountsRepository,
)
from repositories.database.analytical_structures_repository import (
    AnalyticalStructuresRepository,
)
from repositories.database.courses_repository import CoursesRepository
from repositories.database.divisions_repository import DivisionRepository
from repositories.database.editorials_repository import EditorialsRepository
from repositories.database.languages_repository import LanguagesRepository
from repositories.database.project_states_repository import ProjectStatesRepository
from repositories.database.project_types_repository import ProjectTypesRepository
from repositories.database.publications_types_repository import (
    PublicationsTypesRepository,
)
from repositories.database.purposes_repository import PurposesRepository
from repositories.database.stamps_repository import StampsRepository
from repositories.database.structure_types_repository import StructureTypesRepository
from repositories.database.subjects_repository import SubjectsRepository
from repositories.database.supports_repository import SupportsRepository
from repositories.database.third_party_departments_repository import (
    ThirdPartyDepartmentsRepository,
)
from tests.common import MOCK_OBJECT


class TestMetadataRepositories(unittest.TestCase):
    """
    Test class for Metadata Repositories
    """

    @patch("sqlalchemy.orm.Query.all", return_value=[Courses(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Courses))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_courses(self, mock_get_session, mock_query, mock_all) -> None:
        response = CoursesRepository.get_courses()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Courses)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Courses)

    @patch("sqlalchemy.orm.Query.all", return_value=[Languages(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Languages))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_languages(self, mock_get_session, mock_query, mock_all) -> None:
        response = LanguagesRepository.get_languages()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Languages)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Languages)

    @patch("sqlalchemy.orm.Query.all", return_value=[Stamps(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Stamps))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_stamps(self, mock_get_session, mock_query, mock_all) -> None:
        response = StampsRepository.get_stamps()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Stamps)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Stamps)

    @patch("sqlalchemy.orm.Query.all", return_value=[Subjects(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Subjects))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_subjects(self, mock_get_session, mock_query, mock_all) -> None:
        response = SubjectsRepository.get_subjects()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Subjects)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Subjects)

    @patch("sqlalchemy.orm.Query.all", return_value=[AnalyticalAccounts(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(AnalyticalAccounts))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_analytical_accounts(
        self, mock_get_session, mock_query, mock_all
    ) -> None:
        response = AnalyticalAccountsRepository.get_analytical_accounts()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(AnalyticalAccounts)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], AnalyticalAccounts)

    @patch(
        "sqlalchemy.orm.Query.all", return_value=[AnalyticalStructures(**MOCK_OBJECT)]
    )
    @patch("sqlalchemy.orm.Session.query", return_value=Query(AnalyticalStructures))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_analytical_structures(
        self, mock_get_session, mock_query, mock_all
    ) -> None:
        response = AnalyticalStructuresRepository.get_analytical_structures()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(AnalyticalStructures)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], AnalyticalStructures)

    @patch("sqlalchemy.orm.Query.all", return_value=[Divisions(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Divisions))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_divisions(self, mock_get_session, mock_query, mock_all) -> None:
        response = DivisionRepository.get_division()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Divisions)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Divisions)

    @patch("sqlalchemy.orm.Query.all", return_value=[EditorialArea(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(EditorialArea))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_editorials(self, mock_get_session, mock_query, mock_all) -> None:
        response = EditorialsRepository.get_editorials()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(EditorialArea)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], EditorialArea)

    @patch("sqlalchemy.orm.Query.all", return_value=[ProjectStates(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(ProjectStates))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_project_states(self, mock_get_session, mock_query, mock_all) -> None:
        response = ProjectStatesRepository.get_project_states()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(ProjectStates)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], ProjectStates)

    @patch("sqlalchemy.orm.Query.all", return_value=[ProjectTypes(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(ProjectTypes))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_project_types(self, mock_get_session, mock_query, mock_all) -> None:
        response = ProjectTypesRepository.get_project_types()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(ProjectTypes)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], ProjectTypes)

    @patch("sqlalchemy.orm.Query.all", return_value=[PublicationType(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(PublicationType))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_publication_types(
        self, mock_get_session, mock_query, mock_all
    ) -> None:
        response = PublicationsTypesRepository.get_publications_types()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(PublicationType)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], PublicationType)

    @patch("sqlalchemy.orm.Query.all", return_value=[Purposes(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Purposes))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_purposes(self, mock_get_session, mock_query, mock_all) -> None:
        response = PurposesRepository.get_purposes()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Purposes)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Purposes)

    @patch("sqlalchemy.orm.Query.all", return_value=[StructureTypes(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(StructureTypes))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_structure_types(self, mock_get_session, mock_query, mock_all) -> None:
        response = StructureTypesRepository.get_structure_types()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(StructureTypes)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], StructureTypes)

    @patch("sqlalchemy.orm.Query.all", return_value=[Supports(**MOCK_OBJECT)])
    @patch("sqlalchemy.orm.Session.query", return_value=Query(Supports))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_supports(self, mock_get_session, mock_query, mock_all) -> None:
        response = SupportsRepository.get_supports()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(Supports)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], Supports)

    @patch(
        "sqlalchemy.orm.Query.all", return_value=[ThirdPartyDepartments(**MOCK_OBJECT)]
    )
    @patch("sqlalchemy.orm.Session.query", return_value=Query(ThirdPartyDepartments))
    @patch(
        "repositories.database.manager.database_session_manager.DatabaseSessionManager.get_session",
        return_value=Session(),
    )
    def test_get_third_party_departments(
        self, mock_get_session, mock_query, mock_all
    ) -> None:
        response = ThirdPartyDepartmentsRepository.get_third_party_departments()
        mock_get_session.assert_called_once_with(RDS_NODE_MINERVA_RO_NAME)
        mock_query.assert_called_once_with(ThirdPartyDepartments)
        mock_all.assert_called()

        assert response[0].id == MOCK_OBJECT["id"]
        assert response[0].name == MOCK_OBJECT["name"]
        assert isinstance(response[0], ThirdPartyDepartments)


if __name__ == "__main__":
    unittest.main()
