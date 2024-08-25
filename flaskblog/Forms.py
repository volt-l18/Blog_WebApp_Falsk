from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired ,Length, Email, EqualTo , ValidationError
from flaskblog.models import User

class RegistrationFrom(FlaskForm):
    username = StringField('Username' , validators =[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email' , validators=[DataRequired(),Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password' , validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self , username):
        u = User.query.filter_by(username = username.data).first()
        if u :
            raise ValidationError('This Username is already taken')

    def validate_email(self , email):
        e = User.query.filter_by(username = email.data).first()
        if e :
            raise ValidationError('This Email is already taken')

class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired(),Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username' , validators =[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email' , validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture' , validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self , username):
        if username.data != current_user.username:
            u = User.query.filter_by(username = username.data).first()
            if u :
                raise ValidationError('This Username is already taken')

    def validate_email(self , email):
        if email.data != current_user.email:
            e = User.query.filter_by(username = email.data).first()
            if e :
                raise ValidationError('This Email is already taken')

class PostForm(FlaskForm):
    title = StringField("Title" , validators=[DataRequired()])
    content = TextAreaField('Content' , validators=[DataRequired()])
    submit = SubmitField('Post')
