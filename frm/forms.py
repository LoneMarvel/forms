from frm import app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    description = StringField('Movie Description')
    customer = StringField('Customer')
    category = StringField('Movie Category')
    submit = SubmitField('Save')
