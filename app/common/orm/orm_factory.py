class OrmFactory:
    def __init__(self, orm_initializers_map):
        self.orm_initializers_map = orm_initializers_map

    def get_orm_object(self, orm_name):
        initializer = self.orm_initializers_map.get(orm_name)
        if not initializer:
            raise ValueError(f'the orm name: {orm_name} is not valid or not supported')
        orm_obj = initializer.initialize_orm()
        return orm_obj


class OrmInitializer:
    def __init__(self, orm_name, initializer_func, *func_args, **func_kwargs):
        self.orm_name = orm_name
        self.initializer_func = initializer_func
        self.func_args = func_args
        self.func_kwargs = func_kwargs

    def initialize_orm(self):
        orm_obj = self.initializer_func(*self.func_args, **self.func_kwargs)
        return orm_obj
