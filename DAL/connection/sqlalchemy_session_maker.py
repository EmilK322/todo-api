from typing import Any
from DAL.connection.abc import SessionMaker
from sqlalchemy.orm import sessionmaker
from .exceptions import SessionAlreadyClosedError, SessionAlreadyOpenedError


class SqlAlchemySessionMaker(SessionMaker):
    def __init__(self, engine):
        self._engine = engine
        self._session_maker = sessionmaker(bind=engine)
        self._current_session = None

    def open(self) -> Any:
        if self._current_session is None:
            self._current_session = self._session_maker()
            return self._current_session
        else:
            raise SessionAlreadyOpenedError('session already opened')

    def close(self) -> None:
        if self._current_session is None:
            raise SessionAlreadyClosedError('session already closed')
        else:
            self._current_session.close()
