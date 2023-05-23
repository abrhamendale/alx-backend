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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('3-index.html', home_title=_l("Welcome
                           to Holberton"), home_header=_l("Hello world"))
