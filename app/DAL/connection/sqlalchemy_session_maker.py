from typing import Any
from app.DAL.connection.abc import SessionMaker
from sqlalchemy.orm import sessionmaker, scoped_session


class SqlAlchemySessionMaker(SessionMaker):
    def __init__(self, engine, **session_kwargs):
        self._engine = engine
        self._session_maker = scoped_session(sessionmaker(bind=engine, **session_kwargs))
        self._current_session = None

    def open(self) -> Any:
        session = self._session_maker()
        return session

    def close(self) -> None:
        self._session_maker.remove()
