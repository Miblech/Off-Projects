"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from typing import Dict
from sqlalchemy.orm import Session, scoped_session


class DatabaseSessionManager(object):
    """
    Class DatabaseSessionManager
    """

    def __init__(self, session_factories: Dict[str, scoped_session]):
        self.session_factories = session_factories
        self.sessions: dict[str, scoped_session] = {}

    def get_session(self, db_name: str) -> Session:
        """
        :param db_name: Database name
        :return: Session
        """

        if db_name not in self.sessions:
            if db_name not in self.session_factories:
                raise ValueError(f"Database {db_name} is not configured.")
            self.sessions[db_name] = self.session_factories[db_name]
        return self.sessions[db_name]()

    def close_all(self) -> None:
        """
        :return: None
        """

        for session in self.sessions.values():
            session.remove()
        self.sessions.clear()
