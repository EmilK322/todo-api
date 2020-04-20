import abc
from contextlib import contextmanager


class SessionFactory(abc.ABC):
    @abc.abstractmethod
    def create_session(self):
        pass

    @contextmanager
    @abc.abstractmethod
    def create_session_managed(self):
        pass
