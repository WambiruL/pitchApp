from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title= StringField('Title', validators=[Required()])
    category= SelectField('Category', choices=[('promotion','promotion'),('interview', 'interview'),('product','product'),('game','game')], validators=[Required()])
    pitch=TextAreaField('Your Pitch', validators=[Required()])
    submit=SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment=TextAreaField('Comment', validators=[Required()])
    submit=SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')