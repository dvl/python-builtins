## main python-builtins module

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# from flask_debugtoolbar import DebugToolbarExtension

__all__ = ['app', 'db']
__version__ = 0.2

app = Flask('python-builtins', template_folder='app/templates', static_folder='app/static')
app.config.from_object('app.config')

db = SQLAlchemy(app)

# toolbar = DebugToolbarExtension(app)

from app.controllers import *
from app.handlers import *
from app.routes import *
