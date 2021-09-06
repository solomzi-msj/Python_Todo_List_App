from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TodoField(FlaskForm):
    todo_input = StringField(validators=[DataRequired()])
    # completed = BooleanField('Complete', validators=[DataRequired()])
    submit = SubmitField('Add Todo')