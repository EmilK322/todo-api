import logging

from sqlalchemy import create_engine, Table, Column, Integer, Boolean, String, MetaData
from sqlalchemy.orm import mapper

from app.DAL.connection.abc import SessionFactory, SessionMaker
from app.DAL.connection import SqlAlchemySessionFactory, SqlAlchemySessionMaker
from app.DAL.storage_initializers.abc import StorageInitializer
import config


class SqlAlchemyStorageInitializer(StorageInitializer):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def initialize_storage(self) -> SessionFactory:
        self._logger.info('creating engine object')
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, **config.SQLALCHEMY_ENGINE_KWARGS)
        self._logger.info('creating Metadata object')
        metadata = MetaData()
        self._logger.info('creating SqlAlchemySessionMaker object')
        session_maker: SessionMaker = SqlAlchemySessionMaker(engine, **config.SQLALCHEMY_SESSION_KWARGS)
        self._logger.info('creating SqlAlchemySessionFactory object')
        session_factory: SessionFactory = SqlAlchemySessionFactory(session_maker)
        self._logger.info('start mapping models with SqlAlchemy Tables')
        self._map_models(metadata)
        self._logger.info('finished mapping models with SQlAlchemy Tables')
        self._logger.info('creating all tables')
        metadata.create_all(bind=engine)
        return session_factory

    def _map_models(self, metadata):
        self._logger.debug('importing Todo model locally for mapping')
        from app.BLL.models.todo_model import Todo
        self._logger.info('creating todo table')
        todos = Table('todo', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('text', String),
                      Column('completed', Boolean))
        self._logger.info('map Todo model with todo table')
        mapper(Todo, todos)
