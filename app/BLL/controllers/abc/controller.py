import abc


class Controller(abc.ABC):
    pass


class ReadController(Controller):
    @abc.abstractmethod
    def read(self, *args, **kwargs):
        pass


class CreateController(Controller):
    @abc.abstractmethod
    def create(self, *args, **kwargs):
        pass


class UpdateController(Controller):
    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass


class DeleteController(Controller):
    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass
