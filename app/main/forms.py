from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Enter title',validators=[Required()])
    content = TextAreaField('write pitch', validators=[Required()])
    submit = SubmitField('Submit')

class AddPitch(FlaskForm):
    
    post = TextAreaField('Enter your pitch',validators = [Required()])
    submit = SubmitField('Submit')