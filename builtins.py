# coding: utf-8

import re
try:
    import __builtin__ as builtins
except:
    import builtins
from random import choice

from flask import Flask
from flask import make_response
from flask import render_template

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
        return make_response(render_template('404.html'), 404)

    help_text = getattr(builtins, builtin).__doc__

    return render_template('show.html', builtin=builtin, choices=choices,
                           help=help_text)


if __name__ == '__main__':
    app.run(debug=True)
