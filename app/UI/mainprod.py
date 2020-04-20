import logging
from flask import Flask
from flask_restful import Api
from app.UI.resources import TodoResource
from app.UI.resources import TodoByIdResource

from app.UI.bootstrap import bootstrap_app
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
api = Api(app)
http_server = WSGIServer(('', 8080), app)

if __name__ == '__main__':
    todo_kwargs, todo_by_id_kwargs = bootstrap_app()
    api.add_resource(TodoResource, '/todo', resource_class_kwargs=todo_kwargs)
    api.add_resource(TodoByIdResource, '/todo/<int:todo_id>', resource_class_kwargs=todo_by_id_kwargs)
    logger = logging.getLogger('app')
    logger.info('start running flask app')
    http_server.serve_forever()
