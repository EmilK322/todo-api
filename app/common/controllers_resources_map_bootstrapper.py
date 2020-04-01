from app.controllers.todo_controllers.sqlalchemy_todo_controller import SqlAlchemyTodoController
from app.controllers.todo_by_id_controllers.sqlalchemy_todo_by_id_controller import SqlAlchemyTodoByIdController

todo_kwargs = {
    'controller': SqlAlchemyTodoController()
}

todo_by_id_kwargs = {
    'controller': SqlAlchemyTodoByIdController()
}
