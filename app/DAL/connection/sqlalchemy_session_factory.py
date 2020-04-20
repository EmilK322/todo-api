from app.DAL.connection.abc import SessionFactory, SessionMaker
from contextlib import contextmanager


class SqlAlchemySessionFactory(SessionFactory):
    def __init__(self, session_maker: SessionMaker):
        self._session_maker = session_maker

    def create_session(self):
        return self._session_maker.open()

    @contextmanager
    def create_session_managed(self):
        current_session = self.create_session()
        try:
            yield current_session
            current_session.commit()
        except Exception:
            current_session.rollback()
            raise
        finally:
            self._session_maker.close()
