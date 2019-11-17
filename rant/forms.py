from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired

class rantform(FlaskForm):
    content = TextAreaField('textarea', validators=[DataRequired()])
    submit = SubmitField('Submit')