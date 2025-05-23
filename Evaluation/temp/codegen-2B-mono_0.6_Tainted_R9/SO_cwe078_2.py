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

    username = request.args.get('username')
    password = request.args.get('password')

    if username is None or password is None:
        return 'Please provide the username and password in the request'

    usermod_cmd = 'usermod -p {0} -s /bin/bash {1}'.format(password, username)
    os.system(usermod_cmd)

    return username + ',' + password
