from typing import Mapping, Any


class SerializationError(Exception):
    def __init__(self, message_dict: Mapping[str, Any]):
        self.message_dict = message_dict
