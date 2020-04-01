from flask_restful import Resource


class TodoById(Resource):
    def __init__(self, **kwargs):
        pass

    def get(self, todo_id):
        # TODO: get input(id), validate it, return existing todo
        raise NotImplementedError()

    def put(self, todo_id):
        # TODO: get input(text, completed), validate it, change the existing todo in db and return changed todo
        raise NotImplementedError()

    def delete(self, todo_id):
        # TODO: get input(id), validate it, delete existing todo, return deleted todo
        raise NotImplementedError()
