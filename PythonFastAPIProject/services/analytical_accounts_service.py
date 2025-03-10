"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.analytical_accounts_repository import (
    AnalyticalAccountsRepository,
)


class AnalyticalAccountsService(object):
    """
    Class AnalyticalAccountsService
    """

    @staticmethod
    def get_analytical_accounts() -> GetObjectsResultResponse:
        """
        Get Analytical Accounts
        :Return: GetObjectsResultResponse
        """

        accounts = AnalyticalAccountsRepository.get_analytical_accounts()
        return GetObjectsResultResponse.model_validate({"result": {"data": accounts}})
