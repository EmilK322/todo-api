class ControllerError(Exception):
    pass


class IdNotFoundError(ControllerError):
    pass


class InvalidArgsError(ControllerError):
    pass
