import logging
from typing import Mapping, Any
from .validation_result import ValidationResult
from app.BLL.validation.abc import Validator
from marshmallow import Schema, ValidationError


class MarshmallowValidator(Validator):
    def __init__(self, marshmallow_schema: Schema):
        self._marshmallow_schema: Schema = marshmallow_schema
        self._logger = logging.getLogger(__name__)

    def validate_from_dict(self, input_dict: Mapping[str, Any]) -> ValidationResult:
        try:
            self._logger.info(f'trying to load dictionary')
            obj = self._marshmallow_schema.load(input_dict)
            self._logger.info(f'finished loading dictionary, object: {obj}')
            return ValidationResult(True, obj)
        except ValidationError as err:
            self._logger.exception(f'failed to validate dictionary, {err}')
            return ValidationResult(False, err.normalized_messages())
