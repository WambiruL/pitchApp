from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title= StringField('Title', validators=[Required()])
    category= SelectField('Category', choices=[('promotion','promotion'),('interview', 'interview'),('product','product'),('game','game')], validators=[Required()])
    pitch=TextAreaField('Your Pitch', validators=[Required()])
    submit=SubmitField('Pitch')