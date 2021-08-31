from main_todo.models import Todo

def get_todos() -> list: 
    """Returns a list of todos"""
    todos = Todo.query.order_by(Todo.id).all()
    return todos