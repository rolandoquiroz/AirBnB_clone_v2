#!/usr/bin/python3
"""
Script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__))


@app.teardown_appcontext
def tear_down(self):
    """Tear down method that closes storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Database states listed in a Jinja template"""
    return render_template("7-states_list.html",
                           state_list=storage.all("State"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
