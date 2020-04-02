import logging
import marshmallow as ma
# import like this instead of "from .todo_model import Todo" to prevent circular importing errors
import app.models.sqlalchemy.todo.todo_model as todo_model

_logger = logging.getLogger(__name__)


def validate_id(id):
    _logger.info(f'trying to validate todo_id: {id}')
    _logger.info(f'trying to get todo by id')
    todo = todo_model.Todo.query.get(id)
    if todo is None:
        _logger.error(f'failed to get todo by id: {id}')
        _logger.error(f': failed to validate todo_id: {todo} because id not found')
        raise ma.ValidationError(f'id: {id} not found')

    _logger.info(f'successfully validated todo_id: {todo}')
    _logger.debug(f'todo_id belongs to todo: {todo}')


def validate_todo_from_dict(dict_input, todo_schema=None):
    _logger.info(f'trying to validate todo object from dictionary: {dict_input}')
    if not todo_schema:
        _logger.debug(f'schema for validation not provided, set it to default "todo_model.TodoSchema()"')
        todo_schema = todo_model.TodoSchema()
    try:
        _logger.info(f'trying to load dictionary')
        todo_obj = todo_schema.load(dict_input)
    except ma.ValidationError as err:
        _logger.error(f'failed to load/validate dictionary as Todo object, dictionary: {dict_input}')
        return False, err
    else:
        _logger.info(f'successfully loaded dictionary')
        _logger.info(f'successfully validated todo from dictionary, todo: {todo_obj}')
        return True, todo_obj
