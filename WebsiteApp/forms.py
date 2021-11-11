from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
    
class RegisterForm(FlaskForm):
    username = StringField ('User name', validators = [DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    confirmPassword = PasswordField ('Confirm Password',validators = [DataRequired()])
    register_button = SubmitField('Register')
    
