from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__version__ = 0.2
__all__ = ['app', 'db']

app = Flask('python-builtins')

app.config['SECRET_KEY'] = 'secr3tk3yl0l'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

app.debug = True

db = SQLAlchemy(app)

from app.controllers import *