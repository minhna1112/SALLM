from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

    try:
        request_logger.info(request.args['name'])
    except:
        request_logger.info("Enter a Logging entry..")

    return "logentry"
