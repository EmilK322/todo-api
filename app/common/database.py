from app.common.orm.orm_object import OrmObject
from app.common.orm.orm_bootstrapper import initialize_orm


orm_obj: OrmObject = initialize_orm()
engine = orm_obj.engine
session = orm_obj.session
Model = orm_obj.model


def initialize_db():
    func_dto = orm_obj.db_init_func_dto
    db_init_func = func_dto.func
    db_init_args = func_dto.args
    db_init_kwargs = func_dto.kwargs
    db_init_func(*db_init_args, **db_init_kwargs)


def close_session():
    func_dto = orm_obj.session_remove_func_dto
    session_remove_func = func_dto.func
    session_remove_args = func_dto.args
    session_remove_kwargs = func_dto.kwargs
    session_remove_func(*session_remove_args, **session_remove_kwargs)
