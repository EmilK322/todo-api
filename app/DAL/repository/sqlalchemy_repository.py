from typing import Mapping, Any, Iterable
from .abc import Repository
from .exceptions import IdNotFoundError
from ..connection.abc import SessionFactory


class SqlAlchemyRepository(Repository):
    def __init__(self, sqlalchemy_entity_class: Any, session_factory: SessionFactory):
        self.sqlalchemy_entity_class = sqlalchemy_entity_class
        self.session_factory = session_factory

    def get_by_id(self, id_) -> Any:
        with self.session_factory.create_session_managed() as session:
            query = self._filter_by_id_query(session, id_)
            entity = query.first()

        if entity is None:
            raise IdNotFoundError(f'id: {id_} not found')
        return entity

    def get_all(self) -> Iterable[Any]:
        with self.session_factory.create_session_managed() as session:
            entities: Iterable[Any] = session.query(self.sqlalchemy_entity_class).all()

        return entities

    def add(self, entity: Any) -> Any:
        with self.session_factory.create_session_managed() as session:
            session.add(entity)
        return entity

    def delete(self, entity: Any) -> Any:
        with self.session_factory.create_session_managed() as session:
            session.delete(entity)
        return entity

    def update(self, entity: Any, **fields: Mapping[str, Any]) -> Any:
        with self.session_factory.create_session_managed() as session:
            for key, value in fields.items():
                entity = self._filter_by_id_query(session, entity.id).first()
                setattr(entity, key, value)
        return entity

    def _filter_by_id_query(self, session, id_):
        query = session.query(self.sqlalchemy_entity_class).filter_by(id=id_)
        return query
