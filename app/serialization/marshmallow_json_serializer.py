from .abc import Serializer
from marshmallow import Schema, ValidationError
from .exception import SerializationError


class MarshmallowJsonSerializer(Serializer):
    def __init__(self, marshmallow_schema: Schema):
        self.marshmallow_schema = marshmallow_schema

    def serialize(self, data):
        try:
            json_serialized = self.marshmallow_schema.dumps(data)
            return json_serialized
        except ValidationError as err:
            message_dict = err.normalized_messages()
            raise SerializationError(message_dict)
