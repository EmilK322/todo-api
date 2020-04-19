import abc
from app.controllers.abc.controller import ReadController, UpdateController, DeleteController


class TodoByIdController(ReadController, UpdateController, DeleteController):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def put(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
