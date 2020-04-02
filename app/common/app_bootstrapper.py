import logging
from app.common.logger.logging_bootstrapper import bootstrap_logging
from app.common.database import initialize_db

_logger = logging.getLogger(__name__)


def bootstrap():
    bootstrap_logging()
    _logger.info('bootstrap logging finished')
    _logger.info('start initializing database')
    initialize_db()
    _logger.info('finished initializing database')
