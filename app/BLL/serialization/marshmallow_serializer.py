from typing import Iterable
from marshmallow import Schema, ValidationError
from .abc import Serializer
from .exception import SerializationError


class MarshmallowSerializer(Serializer):
    def __init__(self, marshmallow_schema: Schema):
        self.marshmallow_schema = marshmallow_schema

    def serialize(self, data):
        try:
            if isinstance(data, Iterable):
                many_flag = True
            else:
                many_flag = False
            serialized = self.marshmallow_schema.dump(data, many=many_flag)
            return serialized
        except ValidationError as err:
            raise SerializationError(err.normalized_messages())
