# coding: utf-8

from app import app

from app.controllers import *

app.add_url_rule('/', 'home', front.index)
