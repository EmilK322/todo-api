import abc
from typing import TypeVar, Generic, Iterable, Mapping, Any

T = TypeVar('T')


class Repository(abc.ABC, Generic[T]):
    @abc.abstractmethod
    def get_by_id(self, id_) -> T:
        pass

    @abc.abstractmethod
    def get_all(self) -> Iterable[T]:
        pass
    
    @abc.abstractmethod
    def add(self, entity: T) -> None:
        pass
    
    @abc.abstractmethod
    def delete(self, entity: T) -> None:
        pass
    
    @abc.abstractmethod
    def update(self, entity: T, **fields: Mapping[str, Any]) -> None:
        pass
