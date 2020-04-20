import config
import logging
import pathlib
from logging.handlers import RotatingFileHandler


def bootstrap_logging():
    path = pathlib.Path(config.ROTATING_LOG_FILE_NAME)
    # creating all parent folders of log files
    path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger('app')
    logger.setLevel(config.LOGGING_LEVEL)
    rotate_file_handler = RotatingFileHandler(config.ROTATING_LOG_FILE_NAME,
                                              maxBytes=config.ROTATING_LOG_FILE_MAX_BYTES,
                                              backupCount=config.ROTATING_LOG_FILE_BACKUP_COUNT)
    formatter = logging.Formatter(config.ROTATING_LOG_FILE_FORMAT)
    rotate_file_handler.setFormatter(formatter)
    logger.addHandler(rotate_file_handler)
    logger.info('logging initialized')
