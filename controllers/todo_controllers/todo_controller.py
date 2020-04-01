import abc
from controllers.controller import GetController, PostController


class TodoController(GetController, PostController):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def post(self, *args, **kwargs):
        pass
