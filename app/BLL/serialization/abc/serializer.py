import abc


class Serializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self, data):
        pass
