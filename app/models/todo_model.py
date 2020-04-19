class Todo:
    def __init__(self, text: str, completed: bool, id: int = None):
        self.id = id
        self.text = text
        self.completed = completed

    def __repr__(self):
        return f'<Todo(id={self.id}, {self.text}, completed={self.completed})>'
