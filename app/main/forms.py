from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Enter title',validators=[Required()])
    content = StringField('write your quote'),validators=[Required()])
    author = TextAreaField('Enter your name', validators=[Required()])
    submit = SubmitField('Submit')