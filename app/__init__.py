## main python-builtins module

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# from flask_debugtoolbar import DebugToolbarExtension

__all__ = ['app', 'db']
__version__ = 0.2

app = Flask('python-builtins', template_folder='app/views', static_folder='public/assets')

app.config['SECRET_KEY'] = 'secr3tk3yl0l'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

app.debug = True

db = SQLAlchemy(app)

# toolbar = DebugToolbarExtension(app)

from app.controllers import *
