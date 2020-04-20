import logging
from typing import Mapping, Any
from .validation_result import ValidationResult
from app.BLL.validation.abc import Validator
from marshmallow import Schema, ValidationError


class MarshmallowValidator(Validator):
    def __init__(self, todo_schema: Schema):
        self._todo_schema: Schema = todo_schema
        self._logger = logging.getLogger(__name__)

    def validate_from_dict(self, input_dict: Mapping[str, Any]) -> ValidationResult:
        try:
            self._logger.info(f'trying to load dictionary')
            todo_obj = self._todo_schema.load(input_dict)
            return ValidationResult(True, todo_obj)
        except ValidationError as err:
            return ValidationResult(False, err.normalized_messages())
