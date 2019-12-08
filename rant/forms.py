from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired

class rantform(FlaskForm):
    password = TextAreaField('Password', validators=[DataRequired()], default="Password to delete post.")
    title = TextAreaField('Title', validators=[DataRequired()], default="Title of post.")
    content = TextAreaField('Content', validators=[DataRequired()], default="Main text of post.")
    submit = SubmitField('Submit')


class deleteform(FlaskForm):
    password = TextAreaField('Password', validators=[DataRequired()], default="ENTER PASSWORD TO DELETE")
    submit = SubmitField('Delete')