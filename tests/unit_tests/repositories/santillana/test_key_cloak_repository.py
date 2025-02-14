"""
    # Created on October 28, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from unittest.mock import patch

import pytest
import requests
from requests import Response

from config import (
    KEYCLOAK_DOMAIN,
    KEYCLOAK_REALM,
    KEYCLOAK_CLIENT_ID,
    KEYCLOAK_SECRET_KEY,
)
from exceptions.unauthorized_exception import UnauthorizedException
from repositories.santillana.key_cloak_repository import KeyCloakRepository
from tests.common import (
    MOCK_RESPONSE_POST_KEYCLOAK,
    MOCK_TOKEN_KEYCLOAK,
    MOCK_TOKEN_KEYCLOAK_INVALID,
    MOCK_RESPONSE_POST_KEYCLOAK_INVALID,
)


@patch.object(Response, "json", return_value=MOCK_TOKEN_KEYCLOAK)
@patch.object(requests, "post", return_value=MOCK_RESPONSE_POST_KEYCLOAK)
def test_check_token(mock_request_post, mock_response_json):
    response = KeyCloakRepository.check_token("TOKEN")

    url = f"{KEYCLOAK_DOMAIN}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token/introspect"

    data = {
        "token": "TOKEN",
        "client_id": KEYCLOAK_CLIENT_ID,
        "client_secret": KEYCLOAK_SECRET_KEY,
    }

    mock_request_post.assert_called_once_with(url, data=data)
    mock_response_json.assert_called_once()
    assert response == MOCK_TOKEN_KEYCLOAK


@patch.object(Response, "json", return_value=MOCK_TOKEN_KEYCLOAK_INVALID)
@patch.object(requests, "post", return_value=MOCK_RESPONSE_POST_KEYCLOAK)
def test_check_token_invalid(mock_request_post, mock_response_json):
    with pytest.raises(UnauthorizedException):
        KeyCloakRepository.check_token("TOKEN")

    url = f"{KEYCLOAK_DOMAIN}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token/introspect"

    data = {
        "token": "TOKEN",
        "client_id": KEYCLOAK_CLIENT_ID,
        "client_secret": KEYCLOAK_SECRET_KEY,
    }

    mock_request_post.assert_called_once_with(url, data=data)
    mock_response_json.assert_called_once()


@patch.object(Response, "json", return_value=MOCK_TOKEN_KEYCLOAK_INVALID)
@patch.object(requests, "post", return_value=MOCK_RESPONSE_POST_KEYCLOAK_INVALID)
def test_check_token_invalid(mock_request_post, mock_response_json):
    with pytest.raises(UnauthorizedException):
        KeyCloakRepository.check_token("TOKEN")

    url = f"{KEYCLOAK_DOMAIN}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token/introspect"

    data = {
        "token": "TOKEN",
        "client_id": KEYCLOAK_CLIENT_ID,
        "client_secret": KEYCLOAK_SECRET_KEY,
    }

    mock_request_post.assert_called_once_with(url, data=data)
    mock_response_json.assert_not_called()
