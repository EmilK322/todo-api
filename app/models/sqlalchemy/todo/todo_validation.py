import marshmallow as ma
# import like this instead of "from .todo_model import Todo" to prevent circular importing errors
import app.models.sqlalchemy.todo.todo_model as todo_model


def validate_id(id):
    todo = todo_model.Todo.query.get(id)
    if todo is None:
        raise ma.ValidationError(f'id: {id} not found')


def validate_todo_from_dict(dict_input, todo_schema=None):
    if not todo_schema:
        todo_schema = todo_model.TodoSchema()
    try:
        todo_obj = todo_schema.load(dict_input)
    except ma.ValidationError as err:
        return False, err
    else:
        return True, todo_obj
