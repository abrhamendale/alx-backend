#!/usr/bin/env python3
"""App with flask."""


from flask_babel import Babel, lazy_gettext as _l
from flask import Flask, request


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app = Flask(__name__)
babel = Babel(app, BABEL_DEFAULT_LOCALE='en', BABEL_DEFAULT_TIMEZONE='UTC')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('0-index.html', title=_l("Welcome to Holberton"),
                           header=_l("Hello world"))
