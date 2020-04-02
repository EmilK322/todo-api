import logging

from app.common.orm.orm_object import OrmObject
from app.common.orm.orm_bootstrapper import initialize_orm

_logger = logging.getLogger(__name__)

orm_obj: OrmObject = initialize_orm()
engine = orm_obj.engine
session = orm_obj.session
Model = orm_obj.model


def initialize_db():
    _logger.info('extracting db_init function and parameters')
    func_dto = orm_obj.db_init_func_dto
    db_init_func = func_dto.func
    db_init_args = func_dto.args
    db_init_kwargs = func_dto.kwargs
    _logger.info('start initializing database')
    db_init_func(*db_init_args, **db_init_kwargs)
    _logger.info('finished initializing database')


def close_session():
    _logger.info('extracting session_remove function and parameters')
    func_dto = orm_obj.session_remove_func_dto
    session_remove_func = func_dto.func
    session_remove_args = func_dto.args
    session_remove_kwargs = func_dto.kwargs
    _logger.info('start removing session')
    session_remove_func(*session_remove_args, **session_remove_kwargs)
    _logger.info('finished removing session')
