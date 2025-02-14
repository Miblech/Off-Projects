"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from http import HTTPStatus
from typing import Callable, Any
from unittest.mock import MagicMock

import pytest
from requests import Response

from models.responses.get_object_response import GetObjectResponse
from models.responses.get_objects_response import (
    GetObjectsResultResponse,
    GetObjectsDataResponse,
)


def parametrize(name: str, args: list[Any]) -> Callable:
    """
    Decorator to parametrize tests
    :param name: Name of the parameter
    :param args: List of arguments
    :return: Wrapper function
    """

    def decorator(func: Callable) -> Callable:
        """
        Decorator to parametrize tests
        :param func: Function to decorate
        :return: Wrapper function
        """

        @pytest.mark.parametrize(name, args)
        def wrapper(*func_args, **func_kwargs) -> None:
            """
            Wrapper function to parametrize tests
            :param func_args: Function arguments
            :param func_kwargs: Function keyword arguments
            """
            self = func_args[0]
            for i in args:
                for rt in func_args:
                    if isinstance(rt, MagicMock):
                        rt.reset_mock()
                with self.subTest(**{name: i}):
                    func_kwargs[name] = i
                    func(*func_args, **func_kwargs)

        return wrapper

    return decorator


MOCK_OBJECT = {
    "id": 1234,
    "name": "Literature",
}

MOCK_OBJECTS = [MOCK_OBJECT]

MOCKED_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MzAxMzI5NzAsImV4cCI6Mjk2MDEzMjk3MCwiZGF0YSI6eyJpZCI6MSwicGxhdGZvcm1faWQiOjEsIm5hbWUiOiJKb3JnZSIsInN1cm5hbWUiOiJTYWVueiIsInJvbGVzIjpbMV19fQ.ZSoPng2IKObh85JMXC4yXtaG1DNTzyPo0jKGHbmVzKI"

MOCKED_TOKEN_DATA = {
    "iat": 1730132970,
    "exp": 2960132970,
    "data": {
        "id": 1,
        "platform_id": 1,
        "name": "Jorge",
        "surname": "Saenz",
        "roles": [1],
    },
}

MOCKED_GET_OBJECT_RESPONSE = GetObjectsResultResponse(
    result=GetObjectsDataResponse(data=[GetObjectResponse(id=1234, name="Literature")]),
    code=0,
    message="",
    **MOCK_OBJECT,
)

MOCK_TOKEN_KEYCLOAK = {
    "exp": 1732788226,
    "iat": 1732787926,
    "jti": "4157f865-4bd9-4420-b470-99f373479764",
    "iss": "https://dev-sso-dpf.santillana.es/realms/flujo_editorial",
    "sub": "afdfbb16-b8fe-4f79-b1b7-27991826960e",
    "typ": "Bearer",
    "azp": "bed1e1a1-db9f-4e3a-b608-9c0aec03fbca",
    "sid": "811cd3b8-a53f-4530-92a8-214a8303ff98",
    "acr": "1",
    "allowed-origins": ["https://dev-dpf.santillana.es"],
    "realm_access": {"roles": ["admin_flujo_editorial"]},
    "scope": "profile email",
    "email_verified": True,
    "name": "Ruben Sanchez-Maroto",
    "preferred_username": "ruben.admin",
    "given_name": "Ruben",
    "family_name": "Sanchez-Maroto",
    "email": "ruben.sanchezmaroto@neoris.com",
    "client_id": "bed1e1a1-db9f-4e3a-b608-9c0aec03fbca",
    "username": "ruben.admin",
    "token_type": "Bearer",
    "active": True,
}

MOCK_TOKEN_KEYCLOAK_INVALID = {"active": False}

MOCK_RESPONSE_POST_KEYCLOAK = Response()
MOCK_RESPONSE_POST_KEYCLOAK.status_code = HTTPStatus.OK.value

MOCK_RESPONSE_POST_KEYCLOAK_INVALID = Response()
MOCK_RESPONSE_POST_KEYCLOAK_INVALID.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
