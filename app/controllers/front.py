# coding: utf-8

from flask import render_template
from sqlalchemy.sql.expression import func

from app.models.builtin import Builtin


def index(builtin=None):
    if not builtin:
        builtin = Builtin.query.order_by(func.random()).first()
    else:
        builtin = Builtin.query.filter(Builtin.name == builtin).first_or_404()

    return render_template('home/index.html', builtin=builtin)
