"""
Import db so database models can be setup and use by postgresql
"""
from movie2archive import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """
    Schema for the user table.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    users = db.relationship(
        "Movielookup", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        """
        represent each item as a string
        """
        return f"#{self.user_id} | Username: {self.username} | Fistname: {self.first_name} | Lastname: {self.last_name} | Join date: {self.join_date} "


    def set_password(self, password):
        self.password = generate_password_hash(password)


    def check_password(self,password):
      return check_password_hash(self.password,password)

    
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class Media(db.Model):
    """
    Schema for the media type table.
    """
    media_type_id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.String(20), nullable=False)
    mediatypes = db.relationship(
        "Movielookup", backref="media", cascade="all, delete", lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return self.media_type


class Location(db.Model):
    """
    Schema for the location table.
    """
    location_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20), nullable=False)
    locations = db.relationship(
        "Movielookup", backref="location", cascade="all, delete", lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return self.location


class Edition(db.Model):
    """
    Schema for the edition table.
    """
    edition_id = db.Column(db.Integer, primary_key=True)
    edition = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return self.edition


class Movielookup(db.Model):
    """
    Schema for the movie lookup table.
    """
    movie_lookup_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
            "user.user_id", ondelete="CASCADE"), nullable=False)
    movie_id = db.Column(db.String(100), nullable=False)
    imdbID = db.Column(db.String(50), nullable=True)
    movie_title = db.Column(db.String(260), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey(
            "location.location_id", ondelete="CASCADE"), nullable=False)
    media_type_id = db.Column(db.Integer, db.ForeignKey(
            "media.media_type_id", ondelete="CASCADE"), nullable=False)
    edition_id = db.Column(db.Integer, nullable=False)
    has_viewed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        """
        represent each item as a string
        """
        return f"# {self.movie_lookup_id} |Movie title: {self.movie_title} | Location: {self.location_id} | Media type: {self.media_type_id} | Edition: {self.edition_id} | Viewed: {self.has_viewed}"
