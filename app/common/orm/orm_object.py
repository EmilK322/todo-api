class OrmObject:
    def __init__(self, engine, session, model, db_init_func_dto, session_remove_func_dto, **extra):
        self.engine = engine
        self.session = session
        self.model = model
        self.db_init_func_dto = db_init_func_dto
        self.session_remove_func_dto = session_remove_func_dto
        self.extra = extra
