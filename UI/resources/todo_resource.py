import logging
from flask_restful import Resource
from flask import request
from app.controllers.abc.todo_controller import TodoController


class TodoResource(Resource):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.controller: TodoController = kwargs['controller']

    def get(self):
        self.logger.info('calling GET')
        self.logger.info('calling controller\'s get method')
        todos = self.controller.get()
        self.logger.info(f'controller finished and returned: {todos}')
        return todos

    def post(self):
        body = request.get_json()
        self.logger.info(f'calling POST with body: {body}')
        self.logger.info(f'calling controller\'s post method')
        new_todo = self.controller.post(**body)
        self.logger.info(f'controller finished and returned: {new_todo}')
        return new_todo
