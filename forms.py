from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, TextField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, Optional, Regexp

#========== inputs for Signup Form for main.py  =========================>


class UserSignup(FlaskForm):
    username = StringField("Username", validators=[Length(
        min=3, max=20, message="That's not a valid username.")])
   
    password = PasswordField("Password",
                             validators=[Length(min=3, max=20, message="That's not a valid password. Must have at lease 3 characters")])

    verify_password = PasswordField("Verify Password",
                                    validators=[Length(min=3, max=20, message="That's not a valid password. Must have at lease 3 characters"),
                                                EqualTo("password", message="Your passwords did not match.")])

    email = StringField("Email (Optional)", validators=[Email()])

    remember = BooleanField("Remember Me")



#==========in puts for Login Form for main.py  =========================>
class UserLogin(FlaskForm):
    username = StringField("Username", validators=[Length(
        min=3, max=20, message="That's not a valid username.")])
  
    password = PasswordField("Password",
                             validators=[Length(min=3, max=20, message="That's not a valid password. Must have at lease 3 characters")])

    
