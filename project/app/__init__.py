from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


# what is the directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    IMAGEFOLDER = os.path.join(basedir,'static','img'),
    # where to store app.db (database file)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)

db = SQLAlchemy(myapp_obj)
login = LoginManager(myapp_obj)
# function that is called to login a user
login.login_view = 'login'

@myapp_obj.before_first_request
def create_tables():
    db.create_all()

from app import routes, models
