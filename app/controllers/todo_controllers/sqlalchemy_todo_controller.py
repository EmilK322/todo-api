import app.models.sqlalchemy.todo.todo_queries as todo_queries
import app.models.sqlalchemy.todo.todo_validation as todo_validation
from app.controllers.todo_controllers.todo_controller import TodoController
from app.models.sqlalchemy.todo.todo_model import TodoSchema
from app.common.http.response.status_codes import StatusCode


class SqlAlchemyTodoController(TodoController):
    def get(self, *args, **kwargs):
        todos = todo_queries.get_all_todos()
        todo_schema = TodoSchema(many=True)
        dumped_todos = todo_schema.dump(todos)
        return dumped_todos, StatusCode.GENERIC_SUCCESS.value

    def post(self, *args, **kwargs):
        todo_schema = TodoSchema()
        # the obj is Todo if succeeded, else it is ValidationError message
        succeeded, obj = todo_validation.validate_todo_from_dict(kwargs)
        if succeeded:
            todo_queries.add_todo(obj)
            ret_obj = todo_schema.dump(obj), StatusCode.SUCCESSFULLY_CREATED.value
        else:
            ret_obj = obj, StatusCode.INVALID_BODY.value
        return ret_obj
