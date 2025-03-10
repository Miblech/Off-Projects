"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import unittest
from unittest.mock import patch, MagicMock
from starlette.testclient import TestClient

from handlers.lambda_handler import app
from models.responses.get_objects_response import GetObjectsResultResponse
from tests.common import MOCKED_GET_OBJECT_RESPONSE, MOCKED_TOKEN_DATA, MOCKED_TOKEN

client = TestClient(app)


class TestRouterV1(unittest.TestCase):
    """
    Test router for Metadata
    """

    @patch(
        "services.stamps_service.StampsService.get_stamps",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_stamps(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/stamps", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.courses_service.CourseService.get_courses",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_courses(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/courses", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.languages_service.LanguagesService.get_languages",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_languages(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/languages", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.subjects_service.SubjectsService.get_subjects",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_subjects(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/subjects", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.analytical_accounts_service.AnalyticalAccountsService.get_analytical_accounts",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_analytical_accounts(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/analytical-accounts",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.analytical_structures_service.AnalyticalStructuresService.get_analytical_structures",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_analytical_structures(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/analytical-structures",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.divisions_service.DivisionsService.get_division",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_divisions(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/divisions", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.editorials_service.EditorialsService.get_editorials",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_editorials(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/editorial-areas",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.project_states_service.ProjectStatesService.get_project_states",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_project_states(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/project-states",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.project_types_service.ProjectTypesService.get_project_types",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_project_types(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/project-types", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.publications_types_service.PublicationsService.get_publications_types",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_publications_types(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/publication-types",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.purposes_service.PurposesService.get_purposes",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_purposes(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/purposes", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.structure_types_service.StructureTypesService.get_structure_types",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_structure_types(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/structure-types",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.supports_service.SupportsService.get_support",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_support(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/supports", headers={"x-auth-token": MOCKED_TOKEN}
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE

    @patch(
        "services.third_party_departments_service.ThirdPartyDepartmentsService.get_third_party_departments",
        return_value=MOCKED_GET_OBJECT_RESPONSE,
    )
    @patch(
        "services.authorization_service.AuthorizationService.authorize_token_keycloak",
        return_value=MOCKED_TOKEN_DATA,
    )
    def test_get_third_party_departments(
        self, mock_authorize_token_keycloak: MagicMock, mock_get_objects: MagicMock
    ) -> None:
        response = client.get(
            url="/mcs/metadata/v1/third-party-departments",
            headers={"x-auth-token": MOCKED_TOKEN},
        )

        mock_get_objects.assert_called_once()
        assert response.status_code == 200
        mock_authorize_token_keycloak.assert_called_once()
        response_model = GetObjectsResultResponse(**response.json())
        assert response_model == MOCKED_GET_OBJECT_RESPONSE


if __name__ == "__main__":
    unittest.main()
