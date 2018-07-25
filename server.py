'''Homepage.'''

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, session
import sys
import os

app = Flask(__name__)
app.secret_key = 'aklgnaeoinboaenfgkahgao'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    '''
    Displays homepage.
    '''
    return render_template('home.html')

@app.route('/outlaws')
def displayOutlaws():
    '''
    Displays outlaws page.
    '''
    return render_template('outlaws.html')

@app.route('/hideout')
def displayHideout():
    '''
    Displays hideout page.
    '''
    return render_template('hideout.html')

@app.route('/code')
def displayCode():
    '''
    Displays code page.
    '''
    return render_template('code.html')

@app.route('/guests')
def displayGuests():
    '''
    Displays guests page.
    '''
    return render_template('guests.html')

@app.route('/availability')
def displayAvailability():
    '''
    Displays availability page.
    '''
    return render_template('availability.html')


if __name__ == '__main__':
    # app.debug = True
    # app.jinja_env.auto_reload = app.debug
    # app.run(host='127.0.0.1', port=8090)

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
