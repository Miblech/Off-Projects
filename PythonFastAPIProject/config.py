"""
 # Created on September 20, 2022, by Neoris
 #
 # Despite this software is developed by Neoris, it belongs to Santillana,
 # either first version of the License, or (at your option) any later version.
 #
"""

from os import environ

K2SDS_LOGGER_LEVEL = "INFO"
MS_NAME = "k2sds-back-metadata"

K2SDS_SECRET_KEY = environ.get("K2SDS_SECRET_KEY", default="my-secret-key")

# Database
RDS_NODE_RO_DATABASE = environ.get(
    "RDS_NODE_RO_DATABASE", default="RDS_NODE_RO_DATABASE"
)
RDS_NODE_RO_ENDPOINT = environ.get(
    "RDS_NODE_RO_ENDPOINT", default="RDS_NODE_RO_ENDPOINT"
)
RDS_NODE_RO_PASSWORD = environ.get(
    "RDS_NODE_RO_PASSWORD", default="RDS_NODE_RO_PASSWORD"
)
RDS_NODE_RO_PORT = int(environ.get("RDS_NODE_RO_PORT", default=3306))
RDS_NODE_RO_USERNAME = environ.get(
    "RDS_NODE_RO_USERNAME", default="RDS_NODE_RO_USERNAME"
)
RDS_NODE_RO_NAME = "K2SDS_RO"

RDS_NODE_RW_DATABASE = environ.get(
    "RDS_NODE_RW_DATABASE", default="RDS_NODE_RW_DATABASE"
)
RDS_NODE_RW_ENDPOINT = environ.get(
    "RDS_NODE_RW_ENDPOINT", default="RDS_NODE_RW_ENDPOINT"
)
RDS_NODE_RW_PASSWORD = environ.get(
    "RDS_NODE_RW_PASSWORD", default="RDS_NODE_RW_PASSWORD"
)
RDS_NODE_RW_PORT = int(environ.get("RDS_NODE_RW_PORT", default=3306))
RDS_NODE_RW_USERNAME = environ.get(
    "RDS_NODE_RW_USERNAME", default="RDS_NODE_RW_USERNAME"
)
RDS_NODE_RW_NAME = "K2SDS_RW"

RDS_NODE_MINERVA_RO_DATABASE = environ.get(
    "RDS_NODE_MINERVA_RO_DATABASE", default="RDS_NODE_MINERVA_RO_DATABASE"
)
RDS_NODE_MINERVA_RO_ENDPOINT = environ.get(
    "RDS_NODE_MINERVA_RO_ENDPOINT", default="RDS_NODE_MINERVA_RO_ENDPOINT"
)
RDS_NODE_MINERVA_RO_PASSWORD = environ.get(
    "RDS_NODE_MINERVA_RO_PASSWORD", default="RDS_NODE_MINERVA_RO_PASSWORD"
)
RDS_NODE_MINERVA_RO_PORT = int(environ.get("RDS_NODE_MINERVA_RO_PORT", default=3306))
RDS_NODE_MINERVA_RO_USERNAME = environ.get(
    "RDS_NODE_MINERVA_RO_USERNAME", default="RDS_NODE_MINERVA_RO_USERNAME"
)
RDS_NODE_MINERVA_RO_NAME = "MINERVA_RO"

RDS_NODE_MINERVA_RW_DATABASE = environ.get(
    "RDS_NODE_MINERVA_RW_DATABASE", default="RDS_NODE_MINERVA_RW_DATABASE"
)
RDS_NODE_MINERVA_RW_ENDPOINT = environ.get(
    "RDS_NODE_MINERVA_RW_ENDPOINT", default="RDS_NODE_MINERVA_RW_ENDPOINT"
)
RDS_NODE_MINERVA_RW_PASSWORD = environ.get(
    "RDS_NODE_MINERVA_RW_PASSWORD", default="RDS_NODE_MINERVA_RW_PASSWORD"
)
RDS_NODE_MINERVA_RW_PORT = int(environ.get("RDS_NODE_MINERVA_RW_PORT", default=3306))
RDS_NODE_MINERVA_RW_USERNAME = environ.get(
    "RDS_NODE_MINERVA_RW_USERNAME", default="RDS_NODE_MINERVA_RW_USERNAME"
)
RDS_NODE_MINERVA_RW_NAME = "MINERVA_RW"

# KEYCLOAK - Default DEV config
KEYCLOAK_REALM = environ.get("KEYCLOAK_REALM", default="KEYCLOAK_REALM")
KEYCLOAK_DOMAIN = environ.get("KEYCLOAK_DOMAIN", default="KEYCLOAK_DOMAIN")
KEYCLOAK_CLIENT_ID = environ.get("KEYCLOAK_CLIENT_ID", default="KEYCLOAK_CLIENT_ID")
KEYCLOAK_SECRET_KEY = environ.get("KEYCLOAK_SECRET_KEY", default="KEYCLOAK_SECRET_KEY")

# Response constants
CODE_RESPONSE_NONE = 0  # No message
CODE_RESPONSE_SUCCESS = 1  # Green
CODE_RESPONSE_WARNING = 2  # Yellow
CODE_RESPONSE_ERROR = 3  # Red

# Logger
VALIDATION_EXCEPTION_DETAIL = (
    "The request body is missing some mandatory fields or the format is invalid. Check the "
    "errors field for more information"
)
RESPONSE_BAD_REQUEST_EXCEPTION = "response.expection.bad_request_exception"
RESPONSE_UNAUTHORIZED_EXCEPTION = "response.unauthorized"
RESPONSE_INTERNAL_SERVER_EXCEPTION = "response.internal_server_error"

# Exceptions
RESPONSE_STAMP_NOT_FOUND_EXCEPTION = (
    "response.metadata-permissions.stamps_not_found_exception"
)
RESPONSE_LANGUAGE_NOT_FOUND_EXCEPTION = (
    "response.metadata-permissions.language_not_found_exception"
)
RESPONSE_SUBJECT_NOT_FOUND_EXCEPTION = (
    "response.metadata-permissions.subject_not_found_exception"
)
RESPONSE_COURSE_NOT_FOUND_EXCEPTION = (
    "response.metadata-permissions.course_not_found_exception"
)

REDIS_HOST = environ.get("REDIS_HOST", default="localhost")
REDIS_PORT = environ.get("REDIS_PORT", default=6379)
REDIS_DB = environ.get("REDIS_DB", default=0)
REDIS_PASSWORD = environ.get("REDIS_PASSWORD", default="")

# Permissions
GET_SUBJECTS = 33
GET_LANGUAGES = 34
GET_STAMPS = 35
GET_COURSES = 36
GET_STRUCTURE_TYPES = 37
GET_PROJECT_TYPES_TAG = 38
GET_SUPPORT = 39
GET_PUBLICATION = 40
GET_DIVISIONS = 41
GET_EDITORIAL_AREAS = 42
GET_PROJECT_STATES = 43
GET_ANALYTICAL_STRUCTURE = 44
GET_PURPOSE = 45
GET_TP_DEPARTMENTS = 46
GET_ANALYTICAL_ACCOUNTS = 47
