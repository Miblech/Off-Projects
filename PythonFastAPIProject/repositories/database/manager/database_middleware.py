"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

from repositories.database.manager.database_factory import db_manager


class DatabaseMiddleware(BaseHTTPMiddleware):
    """
    Class DatabaseMiddleware
    """

    async def dispatch(self, request: Request, call_next):
        """
        Middleware to manage database connections
        """

        request.state.db_manager = db_manager
        try:
            response = await call_next(request)
        finally:
            request.state.db_manager.close_all()
        return response
