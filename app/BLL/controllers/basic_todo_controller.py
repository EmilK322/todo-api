import logging

from app.DAL.repository.abc import Repository

from app.BLL.controllers.exception import InvalidArgsError
from app.BLL.controllers.abc import TodoController
from app.BLL.serialization.abc import Serializer
from app.BLL.validation.abc import Validator


class BasicTodoController(TodoController):
    def __init__(self, validator: Validator, serializer: Serializer, repository: Repository):
        self._repository = repository
        self._serializer = serializer
        self._validator = validator
        self._logger = logging.getLogger(__name__)

    def read(self, *args, **kwargs):
        self._logger.info('trying to get all todo records')
        todo_list = self._repository.get_all()
        self._logger.info(f'got all todo records, todos: {todo_list}')
        self._logger.info('trying to serialize all todo records')
        serialized_todo_list = self._serializer.serialize(todo_list)
        self._logger.info(f'finished serializing all todo records, serialized todos: {serialized_todo_list}')
        self._logger.info('return serialized todo list')
        return serialized_todo_list

    def create(self, *args, **kwargs):
        todo_params = kwargs
        self._logger.debug(f'got todo body: {todo_params}')
        self._logger.info('trying to validate dictionary as Todo object')
        validation_result = self._validator.validate_from_dict(todo_params)
        if validation_result.is_valid:
            self._logger.info(f'successfully validated dictionary as Todo object, todo: {validation_result.obj}')
            todo = validation_result.obj
            self._logger.info('trying to add todo to storage')
            created_todo = self._repository.add(todo)
            self._logger.info('finished adding todo to storage')
            serialized_todo = self._serializer.serialize(created_todo)
            self._logger.info('return serialized todo')
            return serialized_todo
        else:
            self._logger.error(f'failed to validate dictionary: {todo_params}')
            err_message = validation_result.obj
            raise InvalidArgsError(err_message)
