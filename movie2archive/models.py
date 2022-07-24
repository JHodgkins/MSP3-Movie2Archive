"""
Import db so database models can be setup and use by postgresql
"""
from datetime import datetime
from movie2archive import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Schema for the User table.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    movies = db.relationship('Movielookup', backref='author', cascade='all, delete',  lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Movielookup(db.Model, UserMixin):
    """
    Schema for the Movie lookup table.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notes = db.Column(db.Text, nullable=True)
    movie_id = db.Column(db.String(100), nullable=True)
    imdbID = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id', ondelete='CASCADE'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id', ondelete='CASCADE'), nullable=False)
    edition_id = db.Column(db.Integer, db.ForeignKey('edition.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.notes}', '{self.date_posted}', '{self.imdbID}')"


class Media(db.Model):
    """
    Schema for the Media type table.
    """
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    mediatypes = db.relationship('Movielookup', backref='media', cascade='all, delete', lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return f"Media('{self.type}')"


class Location(db.Model):
    """
    Schema for the Location table.
    """
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20), nullable=False)
    locationtypes = db.relationship('Movielookup', backref='location', cascade='all, delete', lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return f"Location('{self.location}')"

class Edition(db.Model):
    """
    Schema for the Editiona table.
    """
    id = db.Column(db.Integer, primary_key=True)
    edition = db.Column(db.String(50), nullable=False)
    editiontypes = db.relationship('Movielookup', backref='edition', cascade='all, delete', lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return f"Edition('{self.edition}')"