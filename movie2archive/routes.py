"""
Import flask to habdle routes and render_template to handle template files, flash for message feedback, session to hold user session data and url_for for retrieving base url.
Import Bson so Mongo Id can be read.
Import werkzeug for security measures applied to user account.
Import app to launch, db, mongo from __init__ file for database
details annd connections.
Import Users, MediaType, Location, Edition, Movielookup from the models file.
"""
from flask import (
    Flask, render_template, flash, session, url_for)
from bson.objectid import ObjectId
from movie2archive import app, db, mongo
from movie2archive.models import (
    User, Media, MovieLookup)


@app.route("/")
def home():
    """ render a landing page for when user visits Movie2Archive."""
    return render_template("index.html", )


@app.route("/about")
def about():
    """ render a landing page for when user visits Movie2Archive."""
    return render_template('about.html', title='About') 


@app.route("/login")
def login():
    """ render a landing page for when user visits Movie2Archive."""
    return render_template('login.html', title='Login') 


@app.route("/register")
def register():
    """ render a landing page for when user visits Movie2Archive."""
    return render_template('register.html', title='Register') 


# testing mongo connection
@app.route("/get_movies")
def get_movies():
    movies = mongo.db.movies.find()
    return render_template("collection.html", movies=movies)
