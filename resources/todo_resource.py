from flask_restful import Resource


class Todo(Resource):
    def __init__(self, **kwargs):
        pass

    def get(self):
        # TODO: return all todos
        raise NotImplementedError()

    def post(self):
        # TODO: get input, validate it, create new todo, return new_todo
        raise NotImplementedError()
