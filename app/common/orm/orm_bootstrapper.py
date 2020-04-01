import config
from app.common.orm.orm_factory import OrmFactory, OrmInitializer
from app.common.orm.sqlalchemy.sqlalchemy_utils import bootstrap_sqlalchemy


def initialize_orm():
    sqlalchemy_initializer = OrmInitializer('sqlalchemy',
                                            bootstrap_sqlalchemy,
                                            config.SQLALCHEMY_DATABASE_URI,
                                            engine_kwargs=config.SQLALCHEMY_ENGINE_KWARGS,
                                            session_kwargs=config.SQLALCHEMY_SESSION_KWARGS)
    orm_initializers = {
        'sqlalchemy': sqlalchemy_initializer
    }
    orm_factory = OrmFactory(orm_initializers)
    orm_object = orm_factory.get_orm_object('sqlalchemy')
    return orm_object
