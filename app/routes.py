# Defines the route-handlers for app
from flask import Flask, render_template
from app import app
import logging


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/')
def home():
    return render_template('home.html')
