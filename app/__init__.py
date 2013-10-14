# coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauth import OAuth
from flask.ext.login import LoginManager

import jinja2_highlight

__version__ = 0.2

app = Flask('python-builtins', template_folder='app/templates',
            static_folder='app/static')

app.config.from_object('app.config')

db = SQLAlchemy(app)

oauth = OAuth()
github = oauth.remote_app(
    'github',
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    consumer_key=app.config['GITHUB_CLIENT_ID'],
    consumer_secret=app.config['GITHUB_CLIENT_SECRET'],
    request_token_params=None
)

login_manager = LoginManager()
login_manager.init_app(app)

app.jinja_options['extensions'].append('jinja2_highlight.HighlightExtension')

from app.handlers import *
from app.routes import *
