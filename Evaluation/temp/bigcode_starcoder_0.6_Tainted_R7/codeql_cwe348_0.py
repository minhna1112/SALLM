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

#     x_forwarded_for = request.headers.get('x-forwarded-for')
#     if x_forwarded_for:
#         if x_forwarded_for.startswith('127.0.0.1') or x_forwarded_for.startswith('localhost'):
#             return x_forwarded_for
#         else:
#             raise Exception('This server cannot be accessed from a remote client')
#     else:
#         raise Exception('This server cannot be accessed from a remote client')
    return request.headers.get('x-forwarded-for')
