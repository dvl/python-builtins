# coding: utf-8

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String)
    github_access_token = db.Column(db.Integer)

    examples = db.relationship('Example', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
