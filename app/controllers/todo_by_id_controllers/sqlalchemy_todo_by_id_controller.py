import marshmallow as ma
import app.models.sqlalchemy.todo.todo_queries as todo_queries
import app.models.sqlalchemy.todo.todo_validation as todo_validation
from app.controllers.todo_by_id_controllers.todo_by_id_controller import TodoByIdController
from app.models.sqlalchemy.todo.todo_model import TodoSchema
from app.common.utils import ValidationResult
from app.common.http.response.status_codes import StatusCode


class SqlAlchemyTodoByIdController(TodoByIdController):
    def get(self, *args, **kwargs):
        todo_id = args[0]
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            return validation_result.message, StatusCode.INVALID_ID.value

        todo = todo_queries.get_todo_by_id(todo_id)
        todo_schema = TodoSchema()
        dumped_todo = todo_schema.dump(todo)
        return dumped_todo, StatusCode.GENERIC_SUCCESS.value

    def put(self, *args, **kwargs):
        todo_id = args[0]
        todo_params = kwargs
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            return validation_result.message, StatusCode.INVALID_ID.value

        todo = todo_queries.get_todo_by_id(todo_id)
        succeeded, obj = todo_validation.validate_todo_from_dict(todo_params, TodoSchema(partial=['text', 'completed']))
        if succeeded:
            todo_schema = TodoSchema()
            changed_todo = todo_queries.change_todo(todo, obj)
            ret_val = todo_schema.dump(changed_todo), StatusCode.GENERIC_SUCCESS.value
        else:
            ret_val = obj, StatusCode.INVALID_BODY.value
        return ret_val

    def delete(self, *args, **kwargs):
        todo_id = args[0]
        validation_result = self._validate_todo_id(todo_id)
        if not validation_result.is_valid:
            return validation_result.message, StatusCode.INVALID_BODY.value

        todo = todo_queries.get_todo_by_id(todo_id)
        todo_queries.delete_todo(todo)
        todo_schema = TodoSchema()
        dumped_todo = todo_schema.dump(todo)
        return dumped_todo, StatusCode.GENERIC_SUCCESS.value

    def _validate_todo_id(self, todo_id):
        try:
            todo_validation.validate_id(todo_id)
        except ma.ValidationError as err:
            valid_res = ValidationResult(is_valid=False, message=err.messages)
            return valid_res
        else:
            valid_res = ValidationResult(is_valid=True, message=None)
            return valid_res
