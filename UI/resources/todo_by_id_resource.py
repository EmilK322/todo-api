import logging
from flask_restful import Resource
from flask import request
from app.controllers.abc.todo_by_id_controller import TodoByIdController


class TodoByIdResource(Resource):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.controller: TodoByIdController = kwargs['controller']

    def get(self, todo_id):
        self.logger.info(f'calling GET with todo_id: {todo_id}')
        self.logger.info(f'calling controller\'s get method with todo_id: {todo_id}')
        todo = self.controller.get(todo_id)
        self.logger.info(f'controller finished and returned: {todo}')
        return todo

    def put(self, todo_id):
        body = request.get_json()
        self.logger.info(f'calling PUT with todo_id: {todo_id} and body: {body}')
        self.logger.info('calling controller\'s put method with todo_id and body')
        changed_todo = self.controller.put(todo_id, **body)
        self.logger.info(f'controller finished and returned: {changed_todo}')
        return changed_todo

    def delete(self, todo_id):
        self.logger.info(f'calling DELETE with todo_id: {todo_id}')
        self.logger.info(f'calling controller\'s delete method with todo_id: {todo_id}')
        deleted_todo = self.controller.delete(todo_id)
        self.logger.info(f'controller finished and returned: {deleted_todo}')
        return deleted_todo
