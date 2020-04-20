import logging
from flask_restful import Resource
from flask import request

from app.UI.http_utils.response import StatusCode

from app.BLL.controllers.abc.todo_controller import TodoController
from app.BLL.controllers import InvalidArgsError


class TodoResource(Resource):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.controller: TodoController = kwargs['controller']

    def get(self):
        self.logger.info('calling GET')
        self.logger.info('calling controller\'s get method')
        todo_list = self.controller.read()
        self.logger.info(f'controller finished and returned: {todo_list}')
        return todo_list

    def post(self):
        body = request.get_json()
        self.logger.info(f'calling POST with body: {body}')
        try:
            self.logger.info(f'calling controller\'s post method')
            new_todo = self.controller.create(**body)
            self.logger.info(f'controller finished and returned: {new_todo}')
            return new_todo
        except InvalidArgsError as err:
            return str(err), StatusCode.INVALID_BODY.value
