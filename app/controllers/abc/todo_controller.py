import abc
from app.controllers.abc.controller import ReadController, CreateController


class TodoController(ReadController, CreateController):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def post(self, *args, **kwargs):
        pass
