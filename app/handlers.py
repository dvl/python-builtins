# coding: utf-8

from flask import render_template, session

from app import app, github, login_manager
from app.models.builtin import Builtin
from app.models.user import User


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500


@app.context_processor
def inject_builtins():
    builtins = Builtin.query.all()

    return dict(builtins=builtins)


@github.tokengetter
def get_github_oauth_token():
    return session.get('oauth_token')


@app.context_processor
def inject_user():
    try:
        user = User.by_token(session['oauth_token'][0])
    except KeyError:
        user = None

    return dict(user=user)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
