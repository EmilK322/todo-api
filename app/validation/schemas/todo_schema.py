import logging

import marshmallow as ma
from app.models import Todo


class TodoSchema(ma.Schema):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)

    id = ma.fields.Integer(dump_only=True)
    text = ma.fields.String(required=True)
    completed = ma.fields.Boolean()

    @ma.post_load
    def make_todo(self, data, **kwargs):
        self._logger.debug(f'marshmallow post_load creating Todo object with data: {data}')
        todo = Todo(**data)
        self._logger.debug(f'created todo: {todo}')
        return todo
