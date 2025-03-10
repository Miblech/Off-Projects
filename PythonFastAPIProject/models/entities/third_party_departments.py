"""
    # Created on October 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from sqlalchemy import Column, VARCHAR
from repositories.database.manager.database_factory import Base


class ThirdPartyDepartments(Base):
    __tablename__ = "dpto_terceros"

    id = Column("codigo_sap", VARCHAR(4), primary_key=True)
    name = Column("desc_40", VARCHAR(40))
