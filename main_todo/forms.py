from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoField(FlaskForm):
    todo_input = StringField(validators=[DataRequired()])
    submit = SubmitField('Add Todo')