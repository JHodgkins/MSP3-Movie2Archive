"""
Import required files to initialise the Media2Archive application
"""
import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Check to see if env file exists, load if True
if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from media2archive import routes  # noqa
