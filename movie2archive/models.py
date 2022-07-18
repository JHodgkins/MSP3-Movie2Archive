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
    movies = db.relationship('MovieLookup', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class MovieLookup(db.Model, UserMixin):
    """
    Schema for the MovieLookup table.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    review = db.Column(db.Text, nullable=False)
    imdbID = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.date_posted}', '{self.imdbID}')"


class Media(db.Model):
    """
    Schema for the Media type table.
    """
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    mediatypes = db.relationship('MovieLookup', backref='media', lazy=True)

    def __repr__(self):
        """
        Represent each item as a string
        """
        return f"Media('{self.type}')"