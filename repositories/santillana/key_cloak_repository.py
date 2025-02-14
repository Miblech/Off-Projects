"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from http import HTTPStatus

import requests

from config import (
    KEYCLOAK_DOMAIN,
    KEYCLOAK_REALM,
    KEYCLOAK_CLIENT_ID,
    KEYCLOAK_SECRET_KEY,
    MS_NAME,
)
from exceptions.unauthorized_exception import UnauthorizedException
from logs import logger

CLASS = "KeycloakRepository"


class KeyCloakRepository(object):
    """
    Class KeycloakRepository
    """

    @staticmethod
    def check_token(token: str) -> dict:
        """
        :param str token: Token of SSO Keycloak
        :return: dict
        """

        url = f"{KEYCLOAK_DOMAIN}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token/introspect"

        data = {
            "token": token,
            "client_id": KEYCLOAK_CLIENT_ID,
            "client_secret": KEYCLOAK_SECRET_KEY,
        }

        logger.info(f"[{MS_NAME}][{CLASS}] Checking token in KEYCLOAK: {token}")
        response = requests.post(url, data=data)

        if response.status_code == HTTPStatus.OK.value:
            token_info = response.json()
            if token_info.get("active"):
                logger.info(f"[{MS_NAME}][{CLASS}] Token valid")
                return token_info
            else:
                logger.info(f"[{MS_NAME}][{CLASS}] Token no valid")
                raise UnauthorizedException()
        else:
            logger.error(f"[{MS_NAME}][{CLASS}] Error in validate token")
            raise UnauthorizedException()
