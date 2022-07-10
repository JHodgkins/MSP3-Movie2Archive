"""
Import db so database models can be setup and use by postgresql
"""
from movie2archive import db


class User(db.Model):
    """
    Schema for the user table.
    """
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    join_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        """
        represent each item as a string
        """
        return f"#{self.user_id} | Username: {self.username} | Fistname: {self.first_name} | Lastname: {self.last_name} | Join date: {self.join_date} "


class MediaType(db.Model):
    """
    Schema for the media type table.
    """
    media_type_id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.String(20), nullable=False)

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

    def __repr__(self):
        """
        Represent each item as a string
        """
        return self.media_type


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
        return self.media_type

