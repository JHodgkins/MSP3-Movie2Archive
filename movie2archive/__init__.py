"""
Import required files to initialise the Movie2Archive application
"""
import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

# Check to see if env file exists, load if True
if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# if os.environ.get("DEVELOPMENT") == "True":
#     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
# else:
#     uri = os.environ.get("DATABASE_URL")
#     if uri.startswith("postgres://"):
#         uri = uri.replace("postgres://", "postgresql://", 1)
#     app.config["SQLALCHEMY_DATABASE_URI"] = uri  # Heroku

db = SQLAlchemy(app)
mongo = PyMongo(app)

from movie2archive import routes  # noqa
