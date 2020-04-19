import logging

import app.models.sqlalchemy.todo.todo_queries as todo_queries
import app.models.sqlalchemy.todo.todo_validation as todo_validation
from app.controllers.abc import TodoController
from app.models.todo_model import TodoSchema
from UI.http.response.status_codes import StatusCode


class SqlAlchemyTodoController(TodoController):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get(self, *args, **kwargs):
        self.logger.info('trying to get all todo records')
        todos = todo_queries.get_all_todos()
        self.logger.info(f'got all todo records, todos: {todos}')
        todo_schema = TodoSchema(many=True)
        self.logger.info('trying to dump all todo records')
        dumped_todos = todo_schema.dump(todos)
        self.logger.info(f'finished dumping all todo records, dumped todos: {dumped_todos}')
        self.logger.info('return dumped todo records')
        return dumped_todos, StatusCode.GENERIC_SUCCESS.value

    def post(self, *args, **kwargs):
        todo_schema = TodoSchema()
        # the obj is Todo if succeeded, else it is ValidationError message
        self.logger.info('trying to validate dictionary as Todo object')
        succeeded, obj = todo_validation.validate_todo_from_dict(kwargs)
        if succeeded:
            self.logger.info(f'successfuly validated dictionary as Todo object, todo: {obj}')
            self.logger.info('trying to add todo to db')
            todo_queries.add_todo(obj)
            self.logger.info('finished adding todo to db')
            ret_obj = todo_schema.dump(obj), StatusCode.SUCCESSFULLY_CREATED.value
            self.logger.info('return dumped todo')
        else:
            self.logger.error(f'failed to validate dictionary: {kwargs}')
            ret_obj = obj, StatusCode.INVALID_BODY.value
            self.logger.info('return validation error message')
        return ret_obj
