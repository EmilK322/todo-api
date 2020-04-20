import abc
from typing import Iterable, Mapping, Any


class Repository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id_) -> Any:
        pass

    @abc.abstractmethod
    def get_all(self) -> Iterable[Any]:
        pass
    
    @abc.abstractmethod
    def add(self, entity: Any) -> Any:
        pass
    
    @abc.abstractmethod
    def delete(self, entity: Any) -> Any:
        pass
    
    @abc.abstractmethod
    def update(self, entity: Any, **fields: Mapping[str, Any]) -> Any:
        pass
