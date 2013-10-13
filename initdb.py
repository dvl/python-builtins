# coding: utf-8

import re
try:
    import __builtin__ as builtins
except:
    import builtins

from app import db
from app.models.builtin import Builtin

db.create_all()

re_module = re.compile(r'([a-z]|__import__)')

choices = [i for i in dir(builtins) if re_module.match(i)]

for c in choices:
    db.session.add(Builtin(c, 'n/a', getattr(builtins, c).__doc__ or 'N/A'))
    db.session.commit()

