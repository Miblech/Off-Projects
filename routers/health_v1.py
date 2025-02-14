"""
    # Created on November 12, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from fastapi import APIRouter, Response
from sqlalchemy import text

from config import (
    RDS_NODE_RO_NAME,
    RDS_NODE_RW_NAME,
    RDS_NODE_MINERVA_RO_NAME,
    RDS_NODE_MINERVA_RW_NAME,
)
from logs import logger
from repositories.database.manager.database_factory import db_manager

router = APIRouter()

SELECT_K2SDS = text(
    "SELECT 1 FROM information_schema.TABLES WHERE table_schema = 'k2sds' GROUP BY table_schema"
)
SELECT_MINERVA = text(
    "SELECT 1 FROM information_schema.TABLES WHERE table_schema = 'minerva' GROUP BY table_schema"
)


@router.get("/health", tags=["Health"])
def get_health(response: Response):
    """
    Endpoint to check the health of the service.

    Returns:
        dict: A dictionary with the status of the service and database connections.
    """
    try:
        read_db = (
            db_manager.get_session(RDS_NODE_RO_NAME)
            .connection()
            .execute(SELECT_K2SDS)
            .all()
        )
    except Exception as err:
        logger.error(err)
        read_db = None

    try:
        write_db = (
            db_manager.get_session(RDS_NODE_RW_NAME)
            .connection()
            .execute(SELECT_K2SDS)
            .all()
        )
    except Exception as err:
        logger.error(err)
        write_db = None

    try:
        read_minerva_db = (
            db_manager.get_session(RDS_NODE_MINERVA_RO_NAME)
            .connection()
            .execute(SELECT_MINERVA)
            .all()
        )
    except Exception as err:
        logger.error(err)
        read_minerva_db = None

    try:
        write_minerva_db = (
            db_manager.get_session(RDS_NODE_MINERVA_RW_NAME)
            .connection()
            .execute(SELECT_MINERVA)
            .all()
        )
    except Exception as err:
        logger.error(err)
        write_minerva_db = None

    response.status_code = (
        200 if read_db and write_db and read_minerva_db and write_minerva_db else 500
    )

    return {
        "status": "OK",
        "read_db": "OK" if read_db else "KO",
        "write_db": "OK" if write_db else "KO",
        "read_minerva_db": "OK" if read_minerva_db else "KO",
        "write_minerva_db": "OK" if write_minerva_db else "KO",
    }
