import abc
from typing import Any


class SessionMaker(abc.ABC):
    @abc.abstractmethod
    def open(self) -> Any:
        pass

    @abc.abstractmethod
    def close(self) -> None:
        pass
