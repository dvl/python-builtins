# coding: utf-8

from random import choice

from flask import Flask
from flask import make_response
from flask import render_template

# from pygments import highlight
# from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

choices = [
    'abs', 'divmod', 'input', 'open', 'staticmethod', 'all', 'enumerate',
    'int', 'ord', 'str', 'any', 'eval', 'isinstance', 'pow', 'sum',
    'basestring', 'execfile', 'issubclass', 'print', 'super', 'bin', 'file',
    'iter', 'property', 'tuple', 'bool', 'filter', 'len', 'range', 'type',
    'bytearray', 'float', 'list', 'raw_input', 'unichr', 'callable',
    'format', 'locals', 'reduce', 'unicode', 'chr', 'frozenset', 'long',
    'reload', 'vars', 'classmethod', 'getattr', 'map', 'repr', 'xrange',
    'cmp', 'globals', 'max', 'reversed', 'zip', 'compile', 'hasattr',
    'memoryview', 'round', '__import__', 'complex', 'hash', 'min', 'set',
    'apply', 'delattr', 'help', 'next', 'setattr', 'buffer', 'dict', 'hex',
    'object', 'slice', 'coerce', 'dir', 'id', 'oct', 'sorted', 'intern'
]


@app.route("/")
def index():
    ''' Get a random builtin '''
    return builtin()


@app.route("/<builtin>")
def builtin(builtin=None):
    ''' Get specified builtin or fail '''
    if builtin is None:
        builtin = choice(choices)

    if builtin not in choices:
        return make_response(render_template('404.html'), 404)

    # TODO don't use eval()
    help_text = eval(builtin).__doc__
    # help_text = highlight(eval(builtin).__doc__, PythonLexer(), HtmlFormatter())

    return render_template('show.html', builtin=builtin,
                           choices=sorted(choices), help=help_text,
                           css=HtmlFormatter().get_style_defs('.highlight'))


if __name__ == '__main__':
    app.run(debug=True)
