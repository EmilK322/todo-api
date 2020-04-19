import abc


class Controller(abc.ABC):
    pass


class ReadController(Controller):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass


class CreateController(Controller):
    @abc.abstractmethod
    def post(self, *args, **kwargs):
        pass


class UpdateController(Controller):
    @abc.abstractmethod
    def put(self, *args, **kwargs):
        pass


class DeleteController(Controller):
    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
