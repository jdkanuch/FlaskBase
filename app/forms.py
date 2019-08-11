from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class Form(FlaskForm):
    input_string = StringField('Input Text', validators=Length)
    submit = SubmitField('Submit')
