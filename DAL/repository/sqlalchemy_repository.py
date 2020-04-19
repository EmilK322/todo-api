from typing import Mapping, Any, Iterable
from .abc import Repository, T
from .exceptions import IdNotFoundError
from ..connection.abc import SessionFactory


class SqlAlchemyRepository(Repository[T]):
    def __init__(self, session_factory: SessionFactory):
        self.session_factory = session_factory

    def get_by_id(self, id_) -> T:
        with self.session_factory.create_session_managed() as session:
            entity: T = session.query(T).get(id_)
            if entity is None:
                raise IdNotFoundError(f'id: {id_} not found')

        return entity

    def get_all(self) -> Iterable[T]:
        with self.session_factory.create_session_managed() as session:
            entities: Iterable[T] = session.query(T).all()

        return entities

    def add(self, entity: T) -> None:
        with self.session_factory.create_session_managed() as session:
            session.add(T)

    def delete(self, entity: T) -> None:
        with self.session_factory.create_session_managed() as session:
            session.delete(T)

    def update(self, entity: T, **fields: Mapping[str, Any]) -> None:
        with self.session_factory.create_session_managed() as session:
            entity_attributes_ref = vars(entity)
            for key, value in fields.items():
                entity_attributes_ref[key] = value
