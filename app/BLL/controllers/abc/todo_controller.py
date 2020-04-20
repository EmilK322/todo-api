import abc
from app.BLL.controllers.abc.controller import ReadController, CreateController


class TodoController(ReadController, CreateController):
    @abc.abstractmethod
    def read(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def create(self, *args, **kwargs):
        pass
