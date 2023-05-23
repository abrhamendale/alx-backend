#!/usr/bin/env python3
"""App with flask."""


from flask_babel import Babel
from flask import request, _


class Config(object):
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app, BABEL_DEFAULT_LOCALE='en', BABEL_DEFAULT_TIMEZONE='UTC')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('0-index.html', title=_("Welcome to Holberton"),
                           header=_("Hello world"))
