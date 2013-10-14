# coding: utf-8

import datetime

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    github_id = db.Column(db.Integer)
    github_access_token = db.Column(db.String)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    examples = db.relationship('Example', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')

    def __init__(self, username, github_id, github_access_token):
        self.username = username
        self.github_id = github_id
        self.github_access_token = github_access_token

    @classmethod
    def by_token(self, github_access_token):
        return self.query.filter(self.github_access_token == github_access_token).first()

    @classmethod
    def by_github_id(self, github_id):
        return self.query.filter(self.github_id == github_id).first()

    @classmethod
    def by_username(self, username):
        return self.query.filter(self.username == username).first()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
