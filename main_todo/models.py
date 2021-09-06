from main_todo import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    todo_text = db.Column(db.Text, nullable = False)
    # completed = db.Column(db.Boolean, default = False, nullable = False)

    def __repr__(self):
        return '<Todo %>' % self.id