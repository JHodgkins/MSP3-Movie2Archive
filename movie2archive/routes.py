"""
Import flask to habdle routes and render_template to handle template files.
import app and db from __init__ file
mport Users from the models file
"""
from flask import render_template
from movie2archive import app, db
from movie2archive.models import User, MediaType, Location, Edition


@app.route("/")
def home():
    """Create a tempory route to render main.html content to browser."""
    return render_template("main.html")
