from flask import render_template

from app import app
# from app.models.builtin import Builtin


def index():
    return render_template('base.html')
