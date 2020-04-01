from .todo_model import Todo
from app.common.database import session


def get_all_todos():
    todos = Todo.query.all()
    return todos


def get_todo_by_id(id):
    todo = Todo.query.get(id)
    return todo


def add_todo(todo):
    session.add(todo)
    session.commit()
    return todo


def change_todo_by_id(old_todo_id, new_todo):
    old_todo = get_todo_by_id(old_todo_id)
    changed_todo = change_todo(old_todo, new_todo)
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
    session.delete(todo)
    session.commit()
    return todo


def delete_todo_by_id(id):
    todo = get_todo_by_id(id)
    delete_todo(todo)
    return todo
