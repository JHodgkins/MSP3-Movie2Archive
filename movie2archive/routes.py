"""
Import flask to habdle routes and render_template to handle template files.
Import app and db from __init__ file
Import Users, MediaType, Location, Edition, Movielookup from the models file
"""
from flask import render_template
from movie2archive import app, db
from movie2archive.models import (
    User, Media, Location, Edition, Movielookup)


@app.route("/")
def home():
    """Create a tempory route to render main.html content to browser."""
    return render_template("main.html")
