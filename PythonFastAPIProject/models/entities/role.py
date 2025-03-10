"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from sqlalchemy import Column, Integer, VARCHAR, DATETIME
from repositories.database.manager.database_factory import Base


class Role(Base):
    """
    Class Role
    """

    __tablename__ = "role"

    id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True, nullable=False
    )
    name = Column(VARCHAR(255), nullable=False)
    created_date = Column(DATETIME, nullable=False, server_default="CURRENT_TIMESTAMP")
    updated_date = Column(DATETIME, server_onupdate="CURRENT_TIMESTAMP")
    created_by = Column(VARCHAR(255), nullable=False)
    updated_by = Column(VARCHAR(255))
