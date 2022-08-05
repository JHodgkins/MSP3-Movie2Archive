"""
Import required files to initialise the Movie2Archive application
os so the app can talk to the operating syste.
re  is for regular expression, used when targeting postgreSQL string in Heroku.
Flak framework import into application.
PyMongo so the app can talk to the Mongo database
SQLAlchemy for the database queries.
bcrypt is for hahing strings.
login manager to keep track of logged in session user.
"""
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Check to see if env file exists, load if True
if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # Heroku

# Databases assigned to app
db = SQLAlchemy(app)
mongo = PyMongo(app)

# Bcrypt assignment for hashing passwords
bcrypt = Bcrypt(app)

# LoginManager assignment to app, user views and on-sscreen messages
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# admin stored key for access across site and api key, url and headers for api call
access_key = os.environ.get("ACCKEY")
movie_key = os.environ.get("APIKEY")
apiurl = os.environ.get("APIURL")
headers = {
    "X-RapidAPI-Key": movie_key,
    "X-RapidAPI-Host": "1mdb-data-searching.p.rapidapi.com"
    }

from movie2archive import routes  # noqa
