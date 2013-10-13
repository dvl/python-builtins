# coding: utf-8

from flask import redirect, url_for, session, request, flash

from app import github, db
from app.models.user import User

def login():
    return github.authorize(callback=url_for('authorized', _external=True))


@github.authorized_handler
def authorized(response):
    next_url = request.args.get('next') or url_for('index')

    if response is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    try:
        gh_token = response['access_token']
    except KeyError:
        flash(u'Houve uma falha na autenticação', 'error')
        return redirect(url_for('index'))

    session['oauth_token'] = (gh_token, '')

    gh_data = github.get('/user')
    gh_id, gh_user = (gh_data.data['id'], gh_data.data['login'])

    user = User.by_username(gh_user)

    if user is None:
        user = User(gh_user, gh_id, gh_token)
        db.session.add(user)

    user.username = gh_user
    user.github_id = gh_id
    user.github_access_token = gh_token

    db.session.commit()

    flash(u'Você foi logado!', 'success')
    return redirect(next_url)


def logout():
    session.pop('oauth_token', None)
    flash(u'Você foi deslogado!', 'success')
    return redirect(url_for('index'))
