import logging

from app.DAL.connection.abc import SessionFactory, SessionMaker
from contextlib import contextmanager


class SqlAlchemySessionFactory(SessionFactory):
    def __init__(self, session_maker: SessionMaker):
        self._session_maker = session_maker
        self._logger = logging.getLogger(__name__)

    def create_session(self):
        self._logger.info('opening new session')
        return self._session_maker.open()

    @contextmanager
    def create_session_managed(self):
        self._logger.info('opening new session')
        current_session = self.create_session()
        try:
            self._logger.info('yielding the opened session')
            yield current_session
            self._logger.info('yielding session context ended')
            self._logger.info('committing changes')
            current_session.commit()
        except Exception as err:
            self._logger.exception(f'exception ocurred, doing rollback, Exception: {err}')
            current_session.rollback()
            raise
        finally:
            self._logger.info('closing the opened session')
            self._session_maker.close()
