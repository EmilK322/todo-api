import sqlalchemy as sa
import marshmallow as ma
import app.models.sqlalchemy.todo.todo_validation as validation
from app.common.database import Model


class Todo(Model):
    __tablename__ = 'todo'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.String)
    completed = sa.Column(sa.Boolean)

    def __repr__(self):
        return f'<Todo(id={self.id}, {self.text}, completed={self.completed})>'


class TodoSchema(ma.Schema):
    id = ma.fields.Integer(dump_only=True, validate=validation.validate_id)
    text = ma.fields.String(required=True)
    completed = ma.fields.Boolean()

    @ma.post_load
    def make_todo(self, data, **kwargs):
        return Todo(**data)