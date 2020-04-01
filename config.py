import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'todo_api.sqlite')}"
SQLALCHEMY_ENGINE_KWARGS = {
    'convert_unicode': True
}
SQLALCHEMY_SESSION_KWARGS = {
    'autocommit': False,
    'autoflush': False
}
