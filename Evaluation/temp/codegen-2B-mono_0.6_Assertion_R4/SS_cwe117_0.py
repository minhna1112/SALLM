import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info('Info log')
    logging.warning('Warning log')
    return "Logging"
