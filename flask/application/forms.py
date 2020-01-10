from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from flask_login import LoginManager, current_user


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
            validators=[
                DataRequired()
        ]
    )
    last_name = StringField('Last Name',
            validators=[
                DataRequired()
        ]
    )
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
#Check if the email is already in the email column of the user database
        if user:
            raise ValidationError('Email is already in use!')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
#Check if username is already being used
        if user:
            raise ValidationError('Username is already in use!')



#Create login form
class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
        first_name = StringField('First Name',
            validators=[
                DataRequired(),
                Email()
            ]
        )
        last_name = StringField('Last Name',
            validators=[
                DataRequired(),
                Email()
            ]
        )
        email =StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
        )
        submit = SubmitField('Update')

        def validate_email(self,email):
                if email.data != current_user.email:
                        user = User.query.filter_by(email=email.data).first()
                        if user:
                                raise ValidationError('Email already is use - Please choose another')

