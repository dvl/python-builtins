# coding: utf-8

from flask import render_template


def index():
    return render_template('home/index.html')
