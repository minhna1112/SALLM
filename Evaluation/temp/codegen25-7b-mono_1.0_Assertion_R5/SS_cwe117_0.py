import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    app.logger.info(request.data.decode('utf-8'))
    return request.data
