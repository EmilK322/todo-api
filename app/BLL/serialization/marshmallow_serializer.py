import logging
from typing import Iterable
from marshmallow import Schema, ValidationError
from .abc import Serializer
from .exception import SerializationError


class MarshmallowSerializer(Serializer):
    def __init__(self, marshmallow_schema: Schema):
        self.marshmallow_schema = marshmallow_schema
        self._logger = logging.getLogger(__name__)

    def serialize(self, data):
        self._logger.info(f'trying to serialize data')
        try:
            self._logger.debug(f'checking if data is instance of Iterable')
            if isinstance(data, Iterable):
                self._logger.debug(f'data is instance of Iterable, set many flag to True')
                many_flag = True
            else:
                self._logger.debug(f'data is not instance of Iterable, set many flag to False')
                many_flag = False
            self._logger.info(f'trying to serialize data with marshmallow schema dumping')
            serialized = self.marshmallow_schema.dump(data, many=many_flag)
            self._logger.info(f'finished serialize data with marshmallow schema dumping, serialized_data: {serialized}')
            return serialized
        except ValidationError as err:
            self._logger.exception(f'failed to serialize data, {err}')
            raise SerializationError(err.normalized_messages())
