import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.common.utils import get_self_if_true_or_default, FuncDTO
from app.common.orm.orm_object import OrmObject

_logger = logging.getLogger(__name__)


def bootstrap_sqlalchemy(db_uri, engine_kwargs=None, session_kwargs=None):
    _logger.info('start bootstrapping SqlAlchemy')
    _logger.debug(f'db_uri={db_uri}')
    _logger.debug('trying to get empty dictionaries if engine and session kwargs are None')
    engine_kwargs = get_self_if_true_or_default(engine_kwargs, {})
    session_kwargs = get_self_if_true_or_default(session_kwargs, {})
    _logger.debug(f'engine kwargs={engine_kwargs}, session kwargs={session_kwargs}')
    _logger.info('start creating SqlAlchemy engine')
    engine = create_engine(db_uri, **engine_kwargs)
    _logger.info('finished creating SqlAlchemy engine')
    _logger.debug('check if session kwargs contain "bind" key')
    if 'bind' not in session_kwargs:
        _logger.debug('"bind" key not found in session_kwargs, set "bind" to created engine')
        session_kwargs['bind'] = engine
    _logger.info('creating session')
    db_session = scoped_session(sessionmaker(**session_kwargs))
    _logger.info('creating SqlAlchemy declarative base')
    Base = declarative_base()
    _logger.info('set query property to declarative base object')
    Base.query = db_session.query_property()
    _logger.debug('wrapping database initializing function in FuncDTO')
    init_db_dto = FuncDTO(init_db, engine, Base)
    _logger.debug('wrapping session removing function in FuncDTO')
    session_remove_dto = FuncDTO(remove_session, db_session)
    _logger.info('creating OrmObject with created engine, session, base, init_db_func and session_remove_func')
    orm_obj = OrmObject(engine, db_session, Base, init_db_dto, session_remove_dto)
    return orm_obj


def init_db(engine, Base):
    _logger.info('create all tables associated with declarative_base in the engine database')
    Base.metadata.create_all(bind=engine)


def remove_session(db_session):
    _logger.info('removing session')
    db_session.remove()
