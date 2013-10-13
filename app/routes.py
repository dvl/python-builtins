# coding: utf-8

from app import app

from app.controllers import *

app.add_url_rule('/', 'home', front.index)

app.add_url_rule('/login', 'login', login.login)
app.add_url_rule('/logout', 'logut', login.logout)
app.add_url_rule('/oauth/callback', 'callback', login.authorize)
