from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    first_name = StringField("First Name", validators = [DataRequired()])
    last_name = StringField("Last Name", validators = [DataRequired()])
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    confirm_email = StringField("Confirm Email", validators = [DataRequired(), EqualTo('email')])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField()