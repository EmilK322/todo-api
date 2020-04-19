import abc

from DAL.connection.abc import SessionFactory


class StorageInitializer(abc.ABC):
    @abc.abstractmethod
    def initialize_storage(self) -> SessionFactory:
        pass
