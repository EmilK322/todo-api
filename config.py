import pathlib
import logging

BASE_DIR = str(pathlib.Path.cwd())

SQLALCHEMY_DATABASE_URI = f"sqlite:///{str(pathlib.Path(BASE_DIR) / 'todo_api.sqlite')}"
SQLALCHEMY_ENGINE_KWARGS = {
    'convert_unicode': True
}
SQLALCHEMY_SESSION_KWARGS = {
    'autocommit': False,
    'autoflush': False
}

LOGGING_LEVEL = logging.INFO

ROTATING_LOG_FILE_NAME = f"{str(pathlib.Path(BASE_DIR) / 'logs' / 'logfile.log')}"
ROTATING_LOG_FILE_MAX_BYTES = 2 * 1024 * 1024  # 2MB
ROTATING_LOG_FILE_BACKUP_COUNT = 5
ROTATING_LOG_FILE_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
