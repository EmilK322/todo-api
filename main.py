from flask import Flask
from flask_restful import Api
from app.resources.todo_resource import Todo
from app.resources.todo_by_id_resource import TodoById
from app.common.database import close_session, initialize_db


app = Flask(__name__)
api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    close_session()


api.add_resource(Todo, '/todo')
api.add_resource(TodoById, '/todo/<int:todo_id>')

if __name__ == '__main__':
    initialize_db()
    app.run()


