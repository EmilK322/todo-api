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

    todo_schema: ma.Schema = TodoSchema()
    validator: Validator = MarshmallowValidator(todo_schema)
    serializer: Serializer = MarshmallowSerializer(todo_schema)
    storage_initializer: StorageInitializer = SqlAlchemyStorageInitializer()
    session_factory: SessionFactory = storage_initializer.initialize_storage()
    todo_repository: Repository = SqlAlchemyRepository(Todo, session_factory)
    todo_controller: TodoController = BasicTodoController(validator, serializer, todo_repository)
    todo_by_id_controller: TodoByIdController = BasicTodoByIdController(validator, serializer, todo_repository)

    todo_kwargs = {
        'controller': todo_controller
    }

    todo_by_id_kwargs = {
        'controller': todo_by_id_controller
    }

    return todo_kwargs, todo_by_id_kwargs
