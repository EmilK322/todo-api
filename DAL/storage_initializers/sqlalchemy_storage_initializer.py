from sqlalchemy import create_engine, Table, Column, Integer, Boolean, String, MetaData
from sqlalchemy.orm import mapper

from DAL.connection.abc import SessionFactory, SessionMaker
from DAL.connection import SqlAlchemySessionFactory, SqlAlchemySessionMaker
from DAL.storage_initializers.abc import StorageInitializer
import config


class SqlAlchemyStorageInitializer(StorageInitializer):
    def initialize_storage(self) -> SessionFactory:
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, **config.SQLALCHEMY_ENGINE_KWARGS)
        metadata = MetaData()
        session_maker: SessionMaker = SqlAlchemySessionMaker(engine)
        session_factory: SessionFactory = SqlAlchemySessionFactory(session_maker)
        self._map_models(metadata)
        metadata.create_all(bind=engine)
        return session_factory

    def _map_models(self, metadata):
        from app.models.todo_model import Todo
        todos = Table('todo', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('text', String),
                      Column('completed', Boolean))
        mapper(Todo, todos)
