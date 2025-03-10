"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from fastapi import APIRouter, Header
from typing import Annotated

from config import (
    GET_COURSES,
    GET_SUBJECTS,
    GET_STAMPS,
    GET_STRUCTURE_TYPES,
    GET_PROJECT_TYPES_TAG,
    GET_SUPPORT,
    GET_PUBLICATION,
    GET_DIVISIONS,
    GET_EDITORIAL_AREAS,
    GET_PROJECT_STATES,
    GET_ANALYTICAL_STRUCTURE,
    GET_PURPOSE,
    GET_TP_DEPARTMENTS,
    GET_ANALYTICAL_ACCOUNTS,
    GET_LANGUAGES,
)
from models.responses.get_objects_response import GetObjectsResultResponse
from services.analytical_accounts_service import AnalyticalAccountsService
from services.analytical_structures_service import AnalyticalStructuresService
from services.authorization_service import AuthorizationService
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

router = APIRouter()

COURSE_TAG = "Courses"
LANGUAGE_TAG = "Languages"
SUBJECT_TAG = "Subjects"
STAMP_TAG = "Stamps"
SOCIETIES_TAG = "Societies"
ATTR4_TAG = "Structure Types"
PROJECT_TYPES_TAG = "ProjectTypes"
SUPPORT_TAG = "Support"
PUBLICATION_TAG = "Publication"
DIVISIONS_TAG = "Divisions"
EDITORIAL_AREAS_TAG = "EditorialArea"
PROJECT_STATE_TAG = "ProjectState"
ANALYTICAL_STRUCTURE_TAG = "AnalyticalStructure"
PURPOSES_TAG = "Purpose"
TP_DEPARTMENTS_TAG = "TPDepartments"
ANALYTICAL_ACCOUNTS_TAG = "AnalyticalAccounts"


@router.get("/courses", tags=[COURSE_TAG], response_model=GetObjectsResultResponse)
def get_courses(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all courses available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of courses
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_COURSES)
    return CourseService.get_courses()


@router.get("/languages", tags=[LANGUAGE_TAG], response_model=GetObjectsResultResponse)
def get_languages(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all languages available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of languages
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_LANGUAGES)
    return LanguagesService.get_languages()


@router.get("/subjects", tags=[SUBJECT_TAG], response_model=GetObjectsResultResponse)
def get_subjects(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all subjects available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of subjects
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_SUBJECTS)
    return SubjectsService.get_subjects()


@router.get("/stamps", tags=[STAMP_TAG], response_model=GetObjectsResultResponse)
def get_stamps(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all stamps available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of stamps
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_STAMPS)
    return StampsService.get_stamps()


@router.get(
    "/structure-types", tags=[ATTR4_TAG], response_model=GetObjectsResultResponse
)
def get_structure_types(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all structure types available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of structure types
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_STRUCTURE_TYPES)
    return StructureTypesService.get_structure_types()


@router.get(
    "/project-types", tags=[PROJECT_TYPES_TAG], response_model=GetObjectsResultResponse
)
def get_project_types(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all project types available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of project types
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_PROJECT_TYPES_TAG)
    return ProjectTypesService.get_project_types()


@router.get("/supports", tags=[SUPPORT_TAG], response_model=GetObjectsResultResponse)
def get_supports(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all supports available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of supports
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_SUPPORT)
    return SupportsService.get_support()


@router.get(
    "/publication-types",
    tags=[PUBLICATION_TAG],
    response_model=GetObjectsResultResponse,
)
def get_publications_types(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all publication types available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of publication types
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_PUBLICATION)
    return PublicationsService.get_publications_types()


@router.get("/divisions", tags=[DIVISIONS_TAG], response_model=GetObjectsResultResponse)
def get_divisions(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all divisions available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of divisions
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_DIVISIONS)
    return DivisionsService.get_division()


@router.get(
    "/editorial-areas",
    tags=[EDITORIAL_AREAS_TAG],
    response_model=GetObjectsResultResponse,
)
def get_editorial_areas(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all editorial areas available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of editorial
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_EDITORIAL_AREAS)
    return EditorialsService.get_editorials()


@router.get(
    "/project-states", tags=[PROJECT_STATE_TAG], response_model=GetObjectsResultResponse
)
def get_project_states(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all project states available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of project states
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_PROJECT_STATES)
    return ProjectStatesService.get_project_states()


@router.get(
    "/analytical-structures",
    tags=[ANALYTICAL_STRUCTURE_TAG],
    response_model=GetObjectsResultResponse,
)
def get_analytical_structures(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all analytical structures available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of analytical structures
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(
        x_auth_token, GET_ANALYTICAL_STRUCTURE
    )
    return AnalyticalStructuresService.get_analytical_structures()


@router.get("/purposes", tags=[PURPOSES_TAG], response_model=GetObjectsResultResponse)
def get_purposes(x_auth_token: Annotated[str, Header()]) -> GetObjectsResultResponse:
    """
    Get all purposes available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of purposes
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_PURPOSE)
    return PurposesService.get_purposes()


@router.get(
    "/third-party-departments",
    tags=[TP_DEPARTMENTS_TAG],
    response_model=GetObjectsResultResponse,
)
def get_third_party_departments(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all third-party-departments available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of third-party-departments
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_TP_DEPARTMENTS)
    return ThirdPartyDepartmentsService.get_third_party_departments()


@router.get(
    "/analytical-accounts",
    tags=[ANALYTICAL_ACCOUNTS_TAG],
    response_model=GetObjectsResultResponse,
)
def get_analytical_accounts(
    x_auth_token: Annotated[str, Header()]
) -> GetObjectsResultResponse:
    """
    Get all analytical accounts available in the system.

    \f
    :param str x_auth_token: token that makes the petition
    :return: List of analytical accounts
    :rtype: GetObjectsResultResponse
    """
    AuthorizationService.authorize_token_keycloak(x_auth_token, GET_ANALYTICAL_ACCOUNTS)
    return AnalyticalAccountsService.get_analytical_accounts()
