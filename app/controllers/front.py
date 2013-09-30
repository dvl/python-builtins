from flask import render_template

from app import app
# from app.models.builtin import Builtin


@app.route('/')
def front():
    return render_template('base.html')
