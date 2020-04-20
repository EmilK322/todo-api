import abc
from typing import Mapping, Any

from app.BLL.validation import ValidationResult


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate_from_dict(self, input_dict: Mapping[str, Any]) -> ValidationResult:
        pass
