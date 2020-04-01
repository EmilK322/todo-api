import enum


class StatusCode(enum.Enum):
    GENERIC_SUCCESS = 200
    SUCCESSFULLY_CREATED = 201
    INVALID_BODY = 400
    INVALID_ID = 404
