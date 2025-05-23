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

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    
    if x_forwarded_for is None:
        raise Exception("X-Forwarded-For header is missing")
    
    ip_addresses = [ip.strip() for ip in x_forwarded_for.split(',')]
    
    for ip in ip_addresses:
        if not ip.startswith('192.168'):
            raise Exception("Not a local IP")
    
    return x_forwarded_for
    
    