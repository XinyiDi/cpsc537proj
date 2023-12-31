from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class MusicSearchForm(FlaskForm):
    choices = [('Song', 'Song'),
               ('Artist', 'Artist')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('Search')


