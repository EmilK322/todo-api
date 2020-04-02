import logging


class OrmFactory:
    def __init__(self, orm_initializers_map):
        self.orm_initializers_map = orm_initializers_map
        self._logger = logging.getLogger(__name__)

    def get_orm_object(self, orm_name):
        self._logger.info('trying to get orm initializer based on given orm name')
        initializer = self.orm_initializers_map.get(orm_name)
        if not initializer:
            message = f'the orm name: {orm_name} is not valid or not supported'
            self._logger.error(f'failed to get orm initializer, {message}')
            raise ValueError(message)

        self._logger.info('successfully got orm initializer based on given orm name')
        self._logger.info('return initialize_orm method from orm initializer')
        orm_obj = initializer.initialize_orm()
        return orm_obj


class OrmInitializer:
    def __init__(self, orm_name, initializer_func, *func_args, **func_kwargs):
        self.orm_name = orm_name
        self.initializer_func = initializer_func
        self.func_args = func_args
        self.func_kwargs = func_kwargs
        self._logger = logging.getLogger(__name__)

    def initialize_orm(self):
        self._logger.info('start initializing orm')
        orm_obj = self.initializer_func(*self.func_args, **self.func_kwargs)
        self._logger.info('finished initializing orm')
        return orm_obj
