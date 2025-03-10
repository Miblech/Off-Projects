"""
    # Created on September 20, 2022, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

import logging

from config import K2SDS_LOGGER_LEVEL

# obtain numeric value of environment variable
logger_level = logging.getLevelName(K2SDS_LOGGER_LEVEL)

if len(logging.getLogger().handlers) > 0:
    # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
    # `.basicConfig` does not execute. This we set the level directly.
    logging.getLogger().setLevel(logger_level)
else:
    logging.basicConfig(level=logger_level)
logger = logging.getLogger()

# avoid mysql.connector.plugins unnecessary logs
logging.getLogger("mysql.connector").setLevel(logging.WARNING)
