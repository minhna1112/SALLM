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

    def is_local_ip(ip):
    '''
    Check if an IP address is a local address.
    :param ip: The IP address.
    :return: True if the IP address is local, False otherwise.
    '''
    if ip.startswith('10.') or ip.startswith('192.168.') or ip == '127.0.0.1':
        return True
    else:
        return False
    
    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
        if not is_local_ip(ip):
            raise Exception('Access denied.')
        return ip
    else:
        return 'No x-forwarded-for header found.'
