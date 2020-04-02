import logging
from .todo_model import Todo
from app.common.database import session

_logger = logging.getLogger(__name__)


def get_all_todos():
    _logger.info(f'trying to query Todo for all todo records')
    todos = Todo.query.all()
    _logger.info(f'finished querying Todo records')
    _logger.debug(f'all todo records queried: {todos}')
    return todos


def get_todo_by_id(id):
    _logger.info(f'query Todo for specific todo record with id: {id}')
    todo = Todo.query.get(id)
    _logger.info(f'finished querying Todo record, todo: {todo}')
    return todo


def add_todo(todo):
    _logger.info(f'trying to add Todo record to db, todo: {todo}')
    session.add(todo)
    session.commit()
    _logger.info(f'finished adding Todo record to db, todo: {todo}')
    return todo


def change_todo_by_id(old_todo_id, new_todo):
    _logger.debug(f'change_todo_by_id got params: old_todo_id={old_todo_id} new_todo={new_todo}')
    _logger.info(f'trying to get Todo object by id')
    old_todo = get_todo_by_id(old_todo_id)
    _logger.info(f'got Todo record by id: {old_todo}')
    _logger.info(f'trying to change old todo with new one')
    changed_todo = change_todo(old_todo, new_todo)
    _logger.info(f'finished changing old todo with new one, changed todo: {changed_todo}')
    return changed_todo


def change_todo(old_todo, new_todo):
    _shallow_copy_todo_except_id_and_none(old_todo, new_todo)
    session.commit()
    return old_todo


def _shallow_copy_todo_except_id_and_none(copy_to_todo, copy_from_todo):
    copy_to_todo.text = copy_from_todo.text if copy_from_todo.text else copy_to_todo.text
    copy_to_todo.completed = copy_from_todo.completed if copy_from_todo.completed else copy_to_todo.completed
    return copy_to_todo


def delete_todo(todo):
    _logger.info(f'trying to delete todo: {todo}')
    session.delete(todo)
    session.commit()
    _logger.info(f'finished deleting todo')
    return todo


def delete_todo_by_id(id):
    _logger.info(f'trying to delete todo by id: {id}')
    _logger.info(f'trying to get todo object by id')
    todo = get_todo_by_id(id)
    _logger.info(f'finished getting todo object by id, todo: {todo}')
    _logger.debug('calling delete_todo function')
    delete_todo(todo)
    return todo
