from main_todo import app
from main_todo.forms import TodoField
from main_todo.models import db
from main_todo.models import Todo
from main_todo.helper_functions import get_todos
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    form = TodoField()
    todos = get_todos()
    return render_template('index.html', form = form, todos = todos)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = TodoField()
    if form.validate_on_submit():
        todo_text = Todo(todo_text = form.todo_input.data)
        try:
            db.session.add(todo_text)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'There was an issue adding that todo'
       
@app.route('/delete/<int:id>')
def delete(id: int):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue removing that todo.'