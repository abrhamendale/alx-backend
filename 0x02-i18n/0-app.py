#!/usr/bin/env python3
"""App with flask."""


from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('0-index.html',
                           title="Welcome to Holberton", header="Hello world")
