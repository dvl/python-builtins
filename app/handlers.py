from flask import g, session, render_template

from app import app, github
from app.models.builtin import Builtin
from app.models.user import User


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error/500.html'), 500


@app.context_processor
def inject_builtins():
    builtins = Builtin.query.all()

    return dict(builtins=builtins)


@app.before_request
def before_request():
    g.user = User.query.get(session['user_id']) if 'user_id' in session else None


@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token
