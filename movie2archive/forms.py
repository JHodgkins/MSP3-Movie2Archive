from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SelectField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError)
from movie2archive.models import User, Media


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username has already been taken!.')

    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered on our system, Please use another email address!.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class MediaCatForm(FlaskForm):
    type = StringField('Media type', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add media type')


class EditMediaCatForm(FlaskForm):
    type = StringField('Edit media type', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update media type')


class LocationCatForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add location area')


class EditLocationCatForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update location area')


class EditionCatForm(FlaskForm):
    edition = StringField('Edition type', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Add edition type')


class EditEditionCatForm(FlaskForm):
    edition = StringField('Edition type', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Update edition type')


class MovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired(), Length(min=2, max=100)])
    notes = TextAreaField('Notes about the movie', validators=[DataRequired()])
    media_id = SelectField('Media type', coerce=int)
    location_id = SelectField('Location of collection', coerce=int)
    edition_id = SelectField('Media edition type', coerce=int)
    submit = SubmitField('Add movie to collection')
