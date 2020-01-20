#!/usr/bin/python3
"""
Script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'
