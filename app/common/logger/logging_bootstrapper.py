import config
import logging
from logging.handlers import RotatingFileHandler


def bootstrap_logging():
    logger = logging.getLogger('app')
    logger.setLevel(config.LOGGING_LEVEL)
    rotate_file_handler = RotatingFileHandler(config.ROTATING_LOG_FILE_NAME,
                                              maxBytes=config.ROTATING_LOG_FILE_MAX_BYTES,
                                              backupCount=config.ROTATING_LOG_FILE_BACKUP_COUNT)
    rotate_file_handler.setFormatter(config.ROTATING_LOG_FILE_FORMAT)
    logger.addHandler(rotate_file_handler)
    logger.info('logging initialized')
