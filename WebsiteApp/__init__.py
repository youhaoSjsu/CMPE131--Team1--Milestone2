import os
import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app_Obj = flask.Flask(__name__) 

app_Obj.config.from_mapping (
    SECRET_KEY = 'it-dont-matter',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app_Obj)
login = LoginManager(app_Obj)
login.login_view = 'login'

from WebsiteApp import routes, models