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
    Check if the given IP address is a local IP address.
    :param ip: The IP address to check.
    :return: True if the IP address is local, False otherwise.
    '''
    local_ips = ['127.0.0.1', '::1']
    return ip in local_ips
    
    @app.route('/client_ip')
    def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ips = x_forwarded_for.split(',')
        for ip in ips:
            ip = ip.strip()
            if not is_local_ip(ip):
                raise Exception('Non-local IP detected')
    return x_forwarded_for
