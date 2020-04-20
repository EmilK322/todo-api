import logging
import marshmallow as ma

from app.UI.bootstrap.logging_bootstrapper import bootstrap_logging

from app.BLL.models import Todo

from app.BLL.validation.abc import Validator
from app.BLL.validation.schemas import TodoSchema
from app.BLL.validation import MarshmallowValidator

from app.BLL.serialization.abc import Serializer
from app.BLL.serialization import MarshmallowSerializer

from app.BLL.controllers.abc import TodoController, TodoByIdController
from app.BLL.controllers import BasicTodoController, BasicTodoByIdController

from app.DAL.repository.abc import Repository
from app.DAL.repository import SqlAlchemyRepository

from app.DAL.storage_initializers.abc import StorageInitializer
from app.DAL.storage_initializers import SqlAlchemyStorageInitializer

from app.DAL.connection.abc import SessionFactory


_logger = logging.getLogger(__name__)


def bootstrap_app():
    bootstrap_logging()
    _logger.info('bootstrap logging finished')
    _logger.debug('initializing marshmallow schema of Todo model')
    todo_schema: ma.Schema = TodoSchema()
    _logger.debug('initializing MarshmallowValidator object')
    validator: Validator = MarshmallowValidator(todo_schema)
    _logger.debug('initializing MarshmallowSerializer object')
    serializer: Serializer = MarshmallowSerializer(todo_schema)
    _logger.debug('initializing SqlAlchemyStorageInitializer object')
    storage_initializer: StorageInitializer = SqlAlchemyStorageInitializer()
    _logger.debug('initializing storage and getting SessionFactory for it')
    session_factory: SessionFactory = storage_initializer.initialize_storage()
    _logger.debug('initializing SqlAlchemyRepository object with Todo model')
    todo_repository: Repository = SqlAlchemyRepository(Todo, session_factory)
    _logger.debug('initializing BasicTodoController object')
    todo_controller: TodoController = BasicTodoController(validator, serializer, todo_repository)
    _logger.debug('initializing BasicTodoByIdController object')
    todo_by_id_controller: TodoByIdController = BasicTodoByIdController(validator, serializer, todo_repository)

    _logger.info('mapping controllers to specific resources kwargs')

    todo_kwargs = {
        'controller': todo_controller
    }

    todo_by_id_kwargs = {
        'controller': todo_by_id_controller
    }

    return todo_kwargs, todo_by_id_kwargs
