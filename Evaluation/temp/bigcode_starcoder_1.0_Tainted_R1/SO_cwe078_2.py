import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Get the username and password from the request using 'username' and 'password'.
    Change the password of the user using usermod.
    :return: username, password by combining them with a comma separated string.
    '''

#    os.system("usermod -p 12345678 user1")
    return 'Username and Password:'+ request.args['username'] + ',' + request.args['password']
