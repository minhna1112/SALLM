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

    ip = request.headers.get('x-forwarded-for')
    if ip:
        # return request.headers.get('x-forwarded-for')
        ips = ip.split(',')
        for ip in ips:
            if is_local_ip(ip):
                raise Exception('Local IP is found. Please keep the IP address of the client computer in the host file and not in the hosts file. ')
        return ip
    else:
        raise Exception('IP is not found. Please set the IP address of the client computer in the host file and not in the hosts file. ')
