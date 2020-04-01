import abc


class Controller(abc.ABC):
    pass


class GetController(Controller):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass


class PostController(Controller):
    @abc.abstractmethod
    def post(self, *args, **kwargs):
        pass


class PutController(Controller):
    @abc.abstractmethod
    def put(self, *args, **kwargs):
        pass


class DeleteController(Controller):
    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
