import abc
from app.controllers.abc.controller import GetController, PutController, DeleteController


class TodoByIdController(GetController, PutController, DeleteController):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def put(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
