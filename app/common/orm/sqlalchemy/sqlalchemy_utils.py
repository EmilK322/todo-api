from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.common.utils import get_self_if_true_or_default, FuncDTO
from app.common.orm.orm_object import OrmObject


def bootstrap_sqlalchemy(db_uri, engine_kwargs=None, session_kwargs=None):
    engine_kwargs = get_self_if_true_or_default(engine_kwargs, {})
    session_kwargs = get_self_if_true_or_default(session_kwargs, {})

    engine = create_engine(db_uri, **engine_kwargs)
    if 'bind' not in session_kwargs:
        session_kwargs['bind'] = engine
    db_session = scoped_session(sessionmaker(**session_kwargs))
    Base = declarative_base()
    Base.query = db_session.query_property()

    init_db_dto = FuncDTO(init_db, engine, Base)
    session_remove_dto = FuncDTO(remove_session, db_session)

    orm_obj = OrmObject(engine, db_session, Base, init_db_dto, session_remove_dto)
    return orm_obj


def init_db(engine, Base):
    Base.metadata.create_all(bind=engine)


def remove_session(db_session):
    db_session.remove()
