from flask_restful import Resource
from flask import request
from app.controllers.todo_by_id_controllers.todo_by_id_controller import TodoByIdController


class TodoById(Resource):
    def __init__(self, **kwargs):
        self.controller: TodoByIdController = kwargs['controller']

    def get(self, todo_id):
        todo = self.controller.get(todo_id)
        return todo

    def put(self, todo_id):
        body = request.get_json()
        changed_todo = self.controller.put(todo_id, **body)
        return changed_todo

    def delete(self, todo_id):
        deleted_todo = self.controller.delete(todo_id)
        return deleted_todo
