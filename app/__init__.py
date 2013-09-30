from flask import Flask

__version__ = 0.2

App = Flask('python-builtins')
App.config['SECRET_KEY']
App.debug = True

from app.controllers import *