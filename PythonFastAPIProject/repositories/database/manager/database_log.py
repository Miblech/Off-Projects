"""
    # Created on October 11, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from sqlalchemy.orm import Query

from logs import logger


class DatabaseLog(Query):
    """
    Custom Query class to log the queries and the parameters
    """

    def _iter(self):
        """
        Log the query and the parameters
        """
        logger.info(
            f"Running query: \n{self.statement.compile(
                self.session.get_bind(),
                compile_kwargs={"literal_binds": True})}"
        )
        return super()._iter()
