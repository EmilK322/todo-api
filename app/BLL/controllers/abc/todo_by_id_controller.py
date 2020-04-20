import abc
from app.BLL.controllers.abc.controller import ReadController, UpdateController, DeleteController


class TodoByIdController(ReadController, UpdateController, DeleteController):
    @abc.abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
