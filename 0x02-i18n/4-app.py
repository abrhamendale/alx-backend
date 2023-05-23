#!/usr/bin/env python3
"""App with flask."""


from flask_babel import Babel, lazy_gettext as _l
from flask import Flask, request, render_template


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    user_local = RequestHeader(request).get_user_local()

    if user_local not in app.config.LANGUAGES:
        user_local = app.config["BABEL_DEFAULT_LOCALE"]

    return user_local


@app.route('/')
def index():
    return render_template('3-index.html', home_title=_l("Welcome
                           to Holberton"), home_header=_l("Hello world"))
