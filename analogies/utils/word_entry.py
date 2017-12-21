"""
    Forms to capture text
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SimpleWordEntry(FlaskForm):
    """Simplest form to capture text"""
    text = StringField('Text: ', validators=[DataRequired])
    submit = SubmitField('Submit')
