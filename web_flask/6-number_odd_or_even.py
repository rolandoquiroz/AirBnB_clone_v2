#!/usr/bin/python3
"""
Script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Display “Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    Display “HBNB”
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_(text):
    """
    Display “C *”
    """
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_(text='is_cool'):
    """
    Display “Python *”
    """
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def n_(n):
    """
    Display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return ('{:d} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """
    Display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_template_o_e(n):
    """
    Display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
