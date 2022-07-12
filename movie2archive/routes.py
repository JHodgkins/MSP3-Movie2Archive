"""
Import flask to habdle routes and render_template to handle template files, flash for message feedback, session to hold user session data and url_for for retrieving base url.
Import Bson so Mongo Id can be read.
Import werkzeug for security measures applied to user account.
Import app to launch, db, mongo from __init__ file for database details annd connections.
Import Users, MediaType, Location, Edition, Movielookup from the models file.
"""
from flask import (
    Flask, render_template, flash, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from movie2archive import app, db, mongo
from movie2archive.models import (
    User, Media, Location, Edition, Movielookup)


@app.route("/")
def home():
    """Create a tempory route to render main.html content to browser."""
    return render_template("index.html", )

# testing mongo connection
@app.route("/get_movies")
def get_movies():
    movies = mongo.db.movies.find()
    return render_template("movies-mdbtest.html", movies=movies)