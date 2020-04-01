from flask import Flask
from flask_restful import Api
from app.resources.todo_resource import Todo
from app.resources.todo_by_id_resource import TodoById

app = Flask(__name__)
api = Api(app)


api.add_resource(Todo, '/todo')
api.add_resource(TodoById, '/todo/<int:todo_id>')

if __name__ == '__main__':
    app.run()


