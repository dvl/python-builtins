# coding: utf-8

from app import app

from app.controllers import front, login

app.add_url_rule('/', 'index', front.index)

app.add_url_rule('/login', 'login', login.login)
app.add_url_rule('/logout', 'logout', login.logout)
app.add_url_rule('/login/authorized', 'authorized', login.authorized)
