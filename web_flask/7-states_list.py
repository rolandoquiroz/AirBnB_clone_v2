#!/usr/bin/python3
"""
Hello flask module
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """
    Closes the storage
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    List states in a jinja template
    """
    states_dict = storage.all("State")
    states = states_dict.items()
    return render_template('7-states_list.html', states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
