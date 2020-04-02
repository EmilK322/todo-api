import logging

import marshmallow as ma
import app.models.sqlalchemy.todo.todo_queries as todo_queries
import app.models.sqlalchemy.todo.todo_validation as todo_validation
from app.controllers.todo_by_id_controllers.todo_by_id_controller import TodoByIdController
from app.models.sqlalchemy.todo.todo_model import TodoSchema
from app.common.utils import ValidationResult
from app.common.http.response.status_codes import StatusCode


class SqlAlchemyTodoByIdController(TodoByIdController):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get(self, *args, **kwargs):
        todo_id = args[0]
        self.logger.debug(f'got todo id: {todo_id}')
        self.logger.info(f'trying to validate todo by given id')
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            self.logger.error(f'validation of todo id: {todo_id} failed')
            self.logger.info(f'return error message: {validation_result.message}')
            return validation_result.message, StatusCode.INVALID_ID.value

        self.logger.info('trying to get Todo object by id')
        todo = todo_queries.get_todo_by_id(todo_id)
        self.logger.info(f'successfully got Todo object: {todo}')
        todo_schema = TodoSchema()
        self.logger.info('start dumping todo object')
        dumped_todo = todo_schema.dump(todo)
        self.logger.info(f'finished dumping todo object, dumped: {dumped_todo}')
        return dumped_todo, StatusCode.GENERIC_SUCCESS.value

    def put(self, *args, **kwargs):
        todo_id = args[0]
        todo_params = kwargs
        self.logger.debug(f'got todo id: {todo_id} and body: {todo_params}')
        self.logger.info(f'trying to validate todo by given id')
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            self.logger.error(f'validation of todo id: {todo_id} failed')
            self.logger.info(f'return error message: {validation_result.message}')
            return validation_result.message, StatusCode.INVALID_ID.value

        self.logger.info('trying to get Todo object by id')
        todo = todo_queries.get_todo_by_id(todo_id)
        self.logger.info(f'successfully got Todo object: {todo}')

        self.logger.info('trying to validate dictionary as Todo object')
        succeeded, obj = todo_validation.validate_todo_from_dict(todo_params, TodoSchema(partial=['text', 'completed']))
        if succeeded:
            todo_schema = TodoSchema()
            self.logger.info(f'successfuly validated dictionary as Todo object, todo: {obj}')
            self.logger.info('trying to change todo in db')
            changed_todo = todo_queries.change_todo(todo, obj)
            self.logger.info('finished adding todo to db')
            ret_val = todo_schema.dump(changed_todo), StatusCode.GENERIC_SUCCESS.value
            self.logger.info('return dumped changed todo')
        else:
            self.logger.error(f'failed to validate dictionary: {kwargs}')
            ret_val = obj, StatusCode.INVALID_BODY.value
            self.logger.info('return validation error message')
        return ret_val

    def delete(self, *args, **kwargs):
        todo_id = args[0]
        self.logger.debug(f'got todo id: {todo_id}')
        self.logger.info(f'trying to validate todo by given id')
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            self.logger.error(f'validation of todo id: {todo_id} failed')
            self.logger.info(f'return error message: {validation_result.message}')
            return validation_result.message, StatusCode.INVALID_BODY.value

        self.logger.info('trying to get Todo object by id')
        todo = todo_queries.get_todo_by_id(todo_id)
        self.logger.info(f'successfully got Todo object: {todo}')
        self.logger.info('trying to delete todo')
        todo_queries.delete_todo(todo)
        self.logger.info(f'successfully deleted todo: {todo}')
        todo_schema = TodoSchema()
        self.logger.info('start dumping deleted todo object')
        dumped_todo = todo_schema.dump(todo)
        self.logger.info(f'finished dumping deleted todo object, dumped: {dumped_todo}')
        return dumped_todo, StatusCode.GENERIC_SUCCESS.value

    def _validate_todo_id(self, todo_id):
        try:
            self.logger.info(f'start validating todo id')
            todo_validation.validate_id(todo_id)
        except ma.ValidationError as err:
            self.logger.error(f'failed to validate todo id: {todo_id}, message: {err.messages}')
            valid_res = ValidationResult(is_valid=False, message=err.messages)
            return valid_res
        else:
            self.logger.info('successfully finished validating todo id')
            valid_res = ValidationResult(is_valid=True, message=None)
            return valid_res
