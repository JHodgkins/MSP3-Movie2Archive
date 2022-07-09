"""
Import db so database models can be setup and use by postgresql
"""
from media2archive import db


class Users(db.Model):
    """ Schema for users table. """
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    join_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        """ represent each item as a string """
        return f"#{self.user_id} | Username: {self.username} | Fistname: {self.first_name} | Lastname: {self.last_name} | Join date: {self.join_date} "
