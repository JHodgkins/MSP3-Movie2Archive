"""
FlakForm controls all forms ued by WEForms
current_user returns a callable instance of the logged in
user to check login status.
wtforms import field types imported for use in forms and their validation
wtforms.validators returns types of data to validate against
movie2archive import allows he database models to be called within the page
"""
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    PasswordField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError)
from movie2archive.models import (
    User, Media)


class RegistrationForm(FlaskForm):
    """
    User registration form: Setup form to be displayed on the registration page
    """

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    password2 = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    # Validate username
    def validate_username(self, username):
        """
        Check if user is in database
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username has already been taken!.")

    # Validate email address
    def validate_email(self, email):
        """
        Checks if entered email is in the database
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Email is already registered on our system, \
                    Please use another email address!."
            )


class UpdateUserForm(FlaskForm):
    """
    Update user details form
    """

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Update your details")

    def validate_username(self, username):
        """
        Validate username
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username has already been taken!.")

    def validate_email(self, email):
        """
        validate email address
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "Email is already registered on our system, \
                        Please use another email address!"
                )


class ChangePasswordForm(FlaskForm):
    """
    User change password form
    """

    password = PasswordField(
        "New Password", validators=[DataRequired(), Length(min=8, max=20)]
    )
    password2 = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Change password")


class LoginForm(FlaskForm):
    """
    User login form
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class MediaCatForm(FlaskForm):
    """
    Admin area, add media category form
    """

    type = StringField("Media type", validators=[DataRequired(
        ), Length(min=2, max=20)])
    submit = SubmitField("Add media type")


class EditMediaCatForm(FlaskForm):
    """
    Admin area, edit media category form
    """

    type = StringField(
        "Edit media type", validators=[DataRequired(), Length(min=2, max=20)]
    )
    submit = SubmitField("Update media type")


class LocationCatForm(FlaskForm):
    """
    Admin area, location category form
    """

    location = StringField(
        "Location", validators=[DataRequired(), Length(min=2, max=20)]
    )
    submit = SubmitField("Add location area")


class EditLocationCatForm(FlaskForm):
    """
    Admin area, edit location category form
    """

    location = StringField(
        "Location", validators=[DataRequired(), Length(min=2, max=20)]
    )
    submit = SubmitField("Update location area")


class EditionCatForm(FlaskForm):
    """
    Admin area, edition category form
    """

    edition = StringField(
        "Edition type", validators=[DataRequired(), Length(min=2, max=50)]
    )
    submit = SubmitField("Add edition type")


class EditEditionCatForm(FlaskForm):
    """
    Admin area, edit edition category form
    """

    edition = StringField(
        "Edition type", validators=[DataRequired(), Length(min=2, max=50)]
    )
    submit = SubmitField("Update edition type")


class MovieForm(FlaskForm):
    """
    Collection area, add movie form
    """

    title = StringField(
        "Movie title", validators=[DataRequired(), Length(min=2, max=100)]
    )
    notes = TextAreaField("Notes about the movie", validators=[DataRequired()])
    media_id = SelectField("Media type", coerce=int)
    location_id = SelectField("Location of collection", coerce=int)
    edition_id = SelectField("Media edition type", coerce=int)
    submit = SubmitField("Add movie to collection")


class EditMovieForm(FlaskForm):
    """
    Collection area, edit movie form
    """

    title = StringField(
        "Movie title", validators=[DataRequired(), Length(min=2, max=100)]
    )
    notes = TextAreaField(
        "Update your notes about the movie", validators=[DataRequired()]
    )
    media_id = SelectField("Media type", coerce=int)
    location_id = SelectField("Location of collection", coerce=int)
    edition_id = SelectField("Media edition type", coerce=int)
    submit = SubmitField("Update movie details")
