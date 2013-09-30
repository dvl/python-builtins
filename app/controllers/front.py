from flask import make_response

from app import app
# from app.models.builtin import Builtin

@app.route('/')
def front():
	return make_response('home')