import logging
from app.common.logger.logging_bootstrapper import bootstrap_logging
from app.common.database import initialize_db
logger = logging.getLogger(__name__)


def bootstrap():
    bootstrap_logging()
    logger.info('bootstrap logging finished')
    logger.info('start initializing database')
    initialize_db()
    logger.info('finished initializing database')

