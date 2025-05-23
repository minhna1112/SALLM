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
    
    # Check if both username and password are provided
    if username is None or password is None:
        return 'Must provide both username and password', 400
    
    # Run the command to change the password
    os.system(f"echo {username}:{password} | chpasswd")
    
    return username + "," + password
    
    