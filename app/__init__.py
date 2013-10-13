# coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.github import GithubAuth

__version__ = 0.2

app = Flask('python-builtins', template_folder='app/templates',
            static_folder='app/static')

app.config.from_object('app.config')

db = SQLAlchemy(app)

github = GithubAuth(
    client_id=app.config['GITHUB_CLIENT_ID'],
    client_secret=app.config['GITHUB_CLIENT_SECRET'],
    session_key='user_id'
)

from app.handlers import *
from app.routes import *
