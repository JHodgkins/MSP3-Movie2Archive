"""
Import flask to habdle routes and render_template to handle template files.
import app and db from __init__ file
"""
from flask import render_template
from media2archive import app, db


@app.route("/")
def home():
    """Create a tempory route to render main.html content to browser."""
    return render_template("main.html")
