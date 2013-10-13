# coding: utf-8

import re
try:
    import __builtin__ as builtins
except:
    import builtins
from random import choice

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import make_response

# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter

app = Flask(__name__)

re_module = re.compile(r'([a-z]|__import__)')

choices = [i for i in dir(builtins) if re_module.match(i)]


@app.route("/")
@app.route("/<builtin>")
def builtin(builtin=None):
    ''' Get specified builtin or fail '''
    if builtin is None:
        builtin = choice(choices)

    if builtin not in choices:
        return render_template('404.html'), 404

    help_text = getattr(builtins, builtin).__doc__

    return render_template('show.html', builtin=builtin, choices=choices,
                           help=help_text)

@app.route('/api/v1.0/builtins', methods=['GET'])
def get_builtins():
    resp = []
    for builtin in choices:
        help_text = getattr(builtins, builtin).__doc__
        resp.append({'name': builtin, 'help_text':help_text})
    return jsonify({'builtins': resp})

@app.route('/api/v1.0/builtins/<builtin>', methods=['GET'])
def get_builtin(builtin=None):
    if builtin is None or builtin not in choices:
        return jsonify({'error', 'Resource not found'})
    help_text = getattr(builtins, builtin).__doc__
    resp = {'name': builtin, 'help_text': help_text}
    return jsonify({'builtin': resp})

@app.errorhandler(404)
def not_found(error):
    # REST Errors
    if 'api/v1.0' in request.url:
        return make_response(jsonify( { 'error': 'Not found' } ), 404)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
