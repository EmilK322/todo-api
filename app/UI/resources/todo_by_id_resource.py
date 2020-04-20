import logging
from flask_restful import Resource
from flask import request

from app.UI.http_utils.response import StatusCode

from app.BLL.controllers.abc.todo_by_id_controller import TodoByIdController
from app.BLL.controllers import IdNotFoundError, InvalidArgsError


class TodoByIdResource(Resource):
    def __init__(self, **kwargs):
        self._logger = logging.getLogger(__name__)
        self.controller: TodoByIdController = kwargs['controller']

    def get(self, todo_id):
        self._logger.info(f'calling GET with todo_id: {todo_id}')
        try:
            self._logger.info(f'calling controller\'s get method with todo_id: {todo_id}')
            todo = self.controller.read(todo_id)
            self._logger.info(f'controller finished and returned: {todo}')
            return todo, StatusCode.GENERIC_SUCCESS.value
        except IdNotFoundError as err:
            return str(err), StatusCode.INVALID_ID.value

    def put(self, todo_id):
        body = request.get_json()
        self._logger.info(f'calling PUT with todo_id: {todo_id} and body: {body}')
        try:
            self._logger.info('calling controller\'s put method with todo_id and body')
            changed_todo = self.controller.update(todo_id, **body)
            self._logger.info(f'controller finished and returned: {changed_todo}')
            return changed_todo, StatusCode.GENERIC_SUCCESS.value
        except IdNotFoundError as err:
            return str(err), StatusCode.INVALID_ID.value
        except InvalidArgsError as err:
            return str(err), StatusCode.INVALID_BODY.value

    def delete(self, todo_id):
        self._logger.info(f'calling DELETE with todo_id: {todo_id}')
        try:
            self._logger.info(f'calling controller\'s delete method with todo_id: {todo_id}')
            deleted_todo = self.controller.delete(todo_id)
            self._logger.info(f'controller finished and returned: {deleted_todo}')
            return deleted_todo
        except IdNotFoundError as err:
            return str(err), StatusCode.INVALID_ID.value
