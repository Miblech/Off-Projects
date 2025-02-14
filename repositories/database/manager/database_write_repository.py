"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from sqlite3 import DatabaseError
from config import RDS_NODE_RW_NAME, RDS_NODE_MINERVA_RW_NAME
from repositories.database.manager.database_factory import db_manager


class DatabaseWriteRepository(object):
    """
    Class DatabaseWriteRepository
    """

    node: str

    @classmethod
    def save_object(cls, object_save: object) -> None:
        """
        :param object object_save:
        :return: None
        """

        session = db_manager.get_session(cls.node)
        session.add(object_save)
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            raise
        session.refresh(object_save)

    @classmethod
    def delete_object(cls, object_delete: object) -> None:
        """
        :param object object_delete:
        :return: None
        """

        session = db_manager.get_session(cls.node)
        deleted_object = session.merge(object_delete)
        session.delete(deleted_object)
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            raise

        # We update the object with the new values
        # We do it this way to avoid returning the object
        for attr, value in vars(deleted_object).items():
            setattr(object_delete, attr, value)

    @classmethod
    def update_object(cls, object_update: object) -> None:
        """
        :param object object_update:
        :return: None
        """

        session = db_manager.get_session(cls.node)
        updated_object = session.merge(object_update)
        try:
            session.commit()
        except DatabaseError:
            session.rollback()
            raise

        # We update the object with the new values
        # We do it this way to avoid returning the object
        for attr, value in vars(updated_object).items():
            setattr(object_update, attr, value)


class DatabaseWriteK2sdsRepository(DatabaseWriteRepository):
    """
    Class DatabaseWriteK2sdsRepository
    """

    node = RDS_NODE_RW_NAME


class DatabaseWriteMinervaRepository(DatabaseWriteRepository):
    """
    Class DatabaseWriteMinervaRepository
    """

    node = RDS_NODE_MINERVA_RW_NAME
