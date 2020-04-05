import logging
import config
from app.common.orm.orm_factory import OrmFactory, OrmInitializer
from app.common.orm.sqlalchemy.sqlalchemy_utils import bootstrap_sqlalchemy

_logger = logging.getLogger(__name__)


def initialize_orm():
    _logger.info('start constructing SqlAlchemy orm initializer')
    sqlalchemy_initializer = OrmInitializer('sqlalchemy',
                                            bootstrap_sqlalchemy,
                                            config.SQLALCHEMY_DATABASE_URI,
                                            engine_kwargs=config.SQLALCHEMY_ENGINE_KWARGS,
                                            session_kwargs=config.SQLALCHEMY_SESSION_KWARGS)
    _logger.info('finished constructing SqlAlchemy orm initializer')
    _logger.info('constructing orm_initializers dictionary as {orm_name: orm_initializer}')
    orm_initializers = {
        'sqlalchemy': sqlalchemy_initializer
    }

    _logger.info('creating orm factory and injecting orm_initializers dictionary')
    orm_factory = OrmFactory(orm_initializers)
    _logger.info('trying to get SqlAlchemy\'s orm_object from orm_factory')
    orm_object = orm_factory.get_orm_object('sqlalchemy')
    _logger.info('successfully got SqlAlchemy\'s orm_object from orm_factory')
    return orm_object
