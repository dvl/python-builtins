# coding: utf-8

DEBUG = False
SECRET_KEY = ''

SQLALCHEMY_DATABASE_URI = 'sqlite://'

GITHUB_CLIENT_ID = ''
GITHUB_CLIENT_SECRET = ''

try:
    from local_config import *
except ImportError:
    pass
