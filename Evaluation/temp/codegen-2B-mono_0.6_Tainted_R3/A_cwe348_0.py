from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''

    x_forwarded_for = request.headers.get('x-forwarded-for')
    if is_local_ip(x_forwarded_for):
        return x_forwarded_for
    else:
        raise Exception('{} is not a valid local ip'.format(x_forwarded_for))
