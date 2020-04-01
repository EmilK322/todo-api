from flask_restful import Resource
from flask import request
from app.controllers.todo_controllers.todo_controller import TodoController


class Todo(Resource):
    def __init__(self, **kwargs):
        self.controller: TodoController = kwargs['controller']

    def get(self):
        todos = self.controller.get()
        return todos

    def post(self):
        body = request.get_json()
        new_todo = self.controller.post(**body)
        return new_todo
