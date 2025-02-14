"""
    # Created on October 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from sqlalchemy import Integer, Column, SmallInteger, VARCHAR

from repositories.database.manager.database_factory import Base


class EditorialArea(Base):
    __tablename__ = "peg_area_editorial"

    id = Column("qu_valor_id", Integer, primary_key=True)
    name = Column("qu_descripcion_id", VARCHAR(255), nullable=False)
    state = Column("estado", SmallInteger, nullable=False, default=0)

    publication_editorial_area = None
