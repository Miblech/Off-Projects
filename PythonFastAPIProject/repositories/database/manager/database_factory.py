"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from config import (
    RDS_NODE_RO_DATABASE,
    RDS_NODE_RO_ENDPOINT,
    RDS_NODE_RO_PASSWORD,
    RDS_NODE_RO_PORT,
    RDS_NODE_RO_USERNAME,
    RDS_NODE_RW_DATABASE,
    RDS_NODE_RW_ENDPOINT,
    RDS_NODE_RW_PASSWORD,
    RDS_NODE_RW_PORT,
    RDS_NODE_RW_USERNAME,
    RDS_NODE_MINERVA_RO_DATABASE,
    RDS_NODE_MINERVA_RO_ENDPOINT,
    RDS_NODE_MINERVA_RO_PASSWORD,
    RDS_NODE_MINERVA_RO_PORT,
    RDS_NODE_MINERVA_RO_USERNAME,
    RDS_NODE_MINERVA_RW_DATABASE,
    RDS_NODE_MINERVA_RW_ENDPOINT,
    RDS_NODE_MINERVA_RW_PASSWORD,
    RDS_NODE_MINERVA_RW_PORT,
    RDS_NODE_MINERVA_RW_USERNAME,
    RDS_NODE_RO_NAME,
    RDS_NODE_RW_NAME,
    RDS_NODE_MINERVA_RO_NAME,
    RDS_NODE_MINERVA_RW_NAME,
)
from repositories.database.manager.database_log import DatabaseLog
from repositories.database.manager.database_session_manager import (
    DatabaseSessionManager,
)

DB_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}"
Base = declarative_base()


def get_session_factories() -> Dict[str, scoped_session]:
    """
    :return: Dict[str, scoped_session]
    """

    databases = {
        RDS_NODE_RO_NAME: DB_URL.format(
            RDS_NODE_RO_USERNAME,
            RDS_NODE_RO_PASSWORD,
            RDS_NODE_RO_ENDPOINT,
            RDS_NODE_RO_PORT,
            RDS_NODE_RO_DATABASE,
        ),
        RDS_NODE_RW_NAME: DB_URL.format(
            RDS_NODE_RW_USERNAME,
            RDS_NODE_RW_PASSWORD,
            RDS_NODE_RW_ENDPOINT,
            RDS_NODE_RW_PORT,
            RDS_NODE_RW_DATABASE,
        ),
        RDS_NODE_MINERVA_RO_NAME: DB_URL.format(
            RDS_NODE_MINERVA_RO_USERNAME,
            RDS_NODE_MINERVA_RO_PASSWORD,
            RDS_NODE_MINERVA_RO_ENDPOINT,
            RDS_NODE_MINERVA_RO_PORT,
            RDS_NODE_MINERVA_RO_DATABASE,
        ),
        RDS_NODE_MINERVA_RW_NAME: DB_URL.format(
            RDS_NODE_MINERVA_RW_USERNAME,
            RDS_NODE_MINERVA_RW_PASSWORD,
            RDS_NODE_MINERVA_RW_ENDPOINT,
            RDS_NODE_MINERVA_RW_PORT,
            RDS_NODE_MINERVA_RW_DATABASE,
        ),
    }

    engines = {
        name: create_engine(url, pool_pre_ping=True) for name, url in databases.items()
    }
    return {
        name: scoped_session(
            sessionmaker(
                query_cls=DatabaseLog,
                bind=engine,
                autoflush=name.lower().endswith("rw"),
            )
        )
        for name, engine in engines.items()
    }


session_factories = get_session_factories()
db_manager = DatabaseSessionManager(session_factories)
