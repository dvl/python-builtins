# coding: utf-8

from flask import url_for, session

from app import github


def login():
    if session.get('user_id', None) is None:
        return github.authorize(callback_url=url_for('authorized'))
    else:
        return 'Already logged in'


def logout():
    pass


@github.authorized_handler
def authorize(response):
    pass
