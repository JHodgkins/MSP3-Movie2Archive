from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (
    StringField, TextAreaField, SelectField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError)
from movie2archive.models import User, Media


"""
User registration form
"""
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Validate username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username has already been taken!.')

    # Validate email address
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered on our system, Please use another email address!.')


"""
Update user details form
"""
class UpdateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update your details')

    # Validat username
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username has already been taken!.')

    # Validate email address
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email is already registered on our system, Please use another email address!.')


"""
User login form
"""
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


"""
Admin area, add media category form
"""
class MediaCatForm(FlaskForm):
    type = StringField('Media type', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add media type')


"""
Admin area, edit media category form
"""
class EditMediaCatForm(FlaskForm):
    type = StringField('Edit media type', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update media type')


"""
Admin area, location category form
"""
class LocationCatForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add location area')


"""
Admin area, edit location category form
"""
class EditLocationCatForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update location area')


"""
Admin area, edition category form
"""
class EditionCatForm(FlaskForm):
    edition = StringField('Edition type', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Add edition type')


"""
Admin area, edit edition category form
"""
class EditEditionCatForm(FlaskForm):
    edition = StringField('Edition type', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Update edition type')


"""
Collection area, add movie form
"""
class MovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired(), Length(min=2, max=100)])
    notes = TextAreaField('Notes about the movie', validators=[DataRequired()])
    media_id = SelectField('Media type', coerce=int)
    location_id = SelectField('Location of collection', coerce=int)
    edition_id = SelectField('Media edition type', coerce=int)
    submit = SubmitField('Add movie to collection')


"""
Collection area, edit movie form
"""
class EditMovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired(), Length(min=2, max=100)])
    notes = TextAreaField('Update your notes about the movie', validators=[DataRequired()])
    media_id = SelectField('Media type', coerce=int)
    location_id = SelectField('Location of collection', coerce=int)
    edition_id = SelectField('Media edition type', coerce=int)
    submit = SubmitField('Update movie details')
