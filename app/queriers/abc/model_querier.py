import abc
from typing import Iterable, Any


class ModelQuerier(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> Iterable[Any]:
        pass

    @abc.abstractmethod
    def get_by_id(self, id) -> Any:
        pass

    @abc.abstractmethod
    def get_by_condition(self, **conditions) -> Iterable[Any]:
        pass
