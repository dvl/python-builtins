# coding: utf-8

from flask import Flask
from flask import make_response
from flask import render_template

from random import choice

app = Flask(__name__)

choices = ['abs','divmod','input','open','staticmethod','all','enumerate',
           'int','ord','str','any','eval','isinstance','pow','sum',
           'basestring','execfile','issubclass','print','super','bin','file',
           'iter','property','tuple','bool','filter','len','range','type',
           'bytearray','float','list','raw_input','unichr','callable',
           'format','locals','reduce','unicode','chr','frozenset','long',
           'reload','vars','classmethod','getattr','map','repr','xrange',
           'cmp','globals','max','reversed','zip','compile','hasattr',
           'memoryview','round','__import__','complex','hash','min','set',
           'apply','delattr','help','next','setattr','buffer','dict','hex',
           'object','slice','coerce','dir','id','oct','sorted','intern']


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

    return render_template('show.html', builtin=builtin,
                            help=eval(builtin).__doc__)


if __name__ == '__main__':
    app.run(debug=True)
