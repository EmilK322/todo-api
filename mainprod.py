import logging
from flask import Flask
from flask_restful import Api
from app.resources.todo_resource import Todo
from app.resources.todo_by_id_resource import TodoById
from app.common.database import close_session
from app.common.controllers_resources_map_bootstrapper import todo_kwargs, todo_by_id_kwargs
from app.common.app_bootstrapper import bootstrap
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
api = Api(app)
http_server = WSGIServer(('', 8080), app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    close_session()


api.add_resource(Todo, '/todo', resource_class_kwargs=todo_kwargs)
api.add_resource(TodoById, '/todo/<int:todo_id>', resource_class_kwargs=todo_by_id_kwargs)

if __name__ == '__main__':
    bootstrap()
    logger = logging.getLogger('app')
    logger.info('start running flask app')
    http_server.serve_forever()
