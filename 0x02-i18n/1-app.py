#!/usr/bin/env python3
"""App with flask."""


from flask import Flask
from flask_babel import Babel


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
"""
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
"""
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    return render_template('0-index.html', title="Welcome to Holberton",
                           header="Hello world")
