import logging
from typing import Mapping, Any, Iterable
from .abc import Repository
from .exceptions import IdNotFoundError
from ..connection.abc import SessionFactory


class SqlAlchemyRepository(Repository):
    def __init__(self, sqlalchemy_entity_class: Any, session_factory: SessionFactory):
        self.sqlalchemy_entity_class = sqlalchemy_entity_class
        self.session_factory = session_factory
        self._logger = logging.getLogger(__name__)

    def get_by_id(self, id_) -> Any:
        self._logger.info('creating managed session')
        with self.session_factory.create_session_managed() as session:
            self._logger.info('getting id filtering query')
            query = self._filter_by_id_query(session, id_)
            self._logger.info('getting entity')
            entity = query.first()

        if entity is None:
            self._logger.error(f'id: {id_} not found')
            raise IdNotFoundError(f'id: {id_} not found')
        self._logger.info(f'got entity: {entity}')
        return entity

    def get_all(self) -> Iterable[Any]:
        self._logger.info('creating managed session')
        with self.session_factory.create_session_managed() as session:
            self._logger.info('querying all entities like the given entity')
            entities: Iterable[Any] = session.query(self.sqlalchemy_entity_class).all()
            self._logger.info(f'got entities: {entities}')
        return entities

    def add(self, entity: Any) -> Any:
        self._logger.info('creating managed session')
        with self.session_factory.create_session_managed() as session:
            self._logger.info('adding given entity to storage')
            session.add(entity)

        self._logger.info('entity added to storage')
        return entity

    def delete(self, entity: Any) -> Any:
        self._logger.info('creating managed session')
        with self.session_factory.create_session_managed() as session:
            self._logger.info('deleting given entity from storage')
            session.delete(entity)

        self._logger.info('entity deleted from storage')
        return entity

    def update(self, entity: Any, **fields: Mapping[str, Any]) -> Any:
        self._logger.info('creating managed session')
        with self.session_factory.create_session_managed() as session:
            self._logger.info('start updating entity')
            self._logger.info('got latest version of entity from storage')
            entity = self._filter_by_id_query(session, entity.id).first()
            for key, value in fields.items():
                self._logger.info(f'updating field: {key} with value: {value}')
                setattr(entity, key, value)
        return entity

    def _filter_by_id_query(self, session, id_):
        self._logger.info(f'filtering entities by id: {id_}')
        query = session.query(self.sqlalchemy_entity_class).filter_by(id=id_)
        self._logger.info('got filtering query')
        return query
