# coding: utf-8

import datetime

from app import db


class Builtin(db.Model):
    __tablename__ = 'builtins'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    syntax = db.Column(db.String, nullable=False)
    help = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    examples = db.relationship('Example', back_populates='builtin')
    comments = db.relationship('Comment', back_populates='builtin')

    def __init__(self, name, syntax='N/A', help='N/A'):
        self.name = name
        self.syntax = syntax
        self.help = help

    def __repr__(self):
        return '<Builtin %r>' % (self.name,)


class Example(db.Model):
    __tablename__ = 'examples'

    id = db.Column(db.Integer, primary_key=True)
    builtin_id = db.Column(db.Integer, db.ForeignKey('builtins.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    code = db.Column(db.Text, nullable=False)
    upvote = db.Column(db.Integer, default=0)
    downvote = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    builtin = db.relationship('Builtin', back_populates='examples')
    user = db.relationship('User', back_populates='examples')

    def __init__(self, builtin_id, user_id, code):
        self.builtin_id = builtin_id
        self.user_id = user_id
        self.code = code

    def __repr__(self):
        return '<Example %r>' % (self.id)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    builtin_id = db.Column(db.Integer, db.ForeignKey('builtins.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    builtin = db.relationship('Builtin', back_populates='comments')
    user = db.relationship('User', back_populates='comments')

    def __init__(self, builtin_id, user_id, message):
        self.builtin_id = builtin_id
        self.user_id = user_id
        self.message = message

    def __repr__(self):
        return '<Comment %r>' % (self.id)
