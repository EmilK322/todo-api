import logging

from app.DAL.repository import IdNotFoundError as RepoIdNotFoundError
from app.DAL.repository.abc import Repository

from app.BLL.controllers.exception import InvalidArgsError, IdNotFoundError as ControllerIdNotFoundError
from app.BLL.controllers.abc import TodoByIdController
from app.BLL.serialization.abc import Serializer
from app.BLL.validation.abc import Validator


class BasicTodoByIdController(TodoByIdController):
    def __init__(self, validator: Validator, serializer: Serializer, repository: Repository):
        self._repository = repository
        self._serializer = serializer
        self._validator = validator
        self._logger = logging.getLogger(__name__)

    def read(self, *args, **kwargs):
        todo_id = args[0]
        self._logger.debug(f'got todo id: {todo_id}')
        self._logger.info(f'trying to get todo by given id')
        todo = self._get_todo_by_id(todo_id)
        self._logger.info('start dumping todo object')
        serialized_todo = self._serializer.serialize(todo)
        self._logger.info(f'finished serializing todo object, serialized todo: {serialized_todo}')
        return serialized_todo

    def update(self, *args, **kwargs):
        todo_id = args[0]
        todo_params = kwargs
        self._logger.debug(f'got todo id: {todo_id} and body: {todo_params}')
        self._logger.info(f'trying to get todo by given id')
        todo = self._get_todo_by_id(todo_id)
        validation_result = self._validator.validate_from_dict(todo_params)
        if validation_result.is_valid:
            updated_todo = self._repository.update(todo, **todo_params)
            self._logger.info('start serializing todo object')
            serialized_todo = self._serializer.serialize(updated_todo)
            self._logger.info(f'finished serializing todo object, serialized todo: {serialized_todo}')
            return serialized_todo
        else:
            err_message = validation_result.obj
            raise InvalidArgsError(err_message)

    def delete(self, *args, **kwargs):
        todo_id = args[0]
        self._logger.debug(f'got todo id: {todo_id}')
        self._logger.info(f'trying to get todo by given id')
        todo = self._get_todo_by_id(todo_id)
        deleted_todo = self._repository.delete(todo)
        self._logger.info('start serializing todo object')
        serialized_todo = self._serializer.serialize(deleted_todo)
        self._logger.info(f'finished serializing todo object, serialized todo: {serialized_todo}')
        return serialized_todo

    def _get_todo_by_id(self, todo_id):
        try:
            self._logger.info('trying to get Todo object by id')
            todo = self._repository.get_by_id(todo_id)
            self._logger.info(f'successfully got Todo object: {todo}')
            return todo
        except RepoIdNotFoundError as err:
            raise ControllerIdNotFoundError(str(err))
