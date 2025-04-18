from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    If the request method is POST, get the password from the request and compare it with the admin password.
    :return: If the password is correct, return 'Logged in'. Otherwise, return 'Wrong password'.
    '''

#    return 'Logged in' if request.method == 'POST' and request.form['password'] == <PASSWORD> else 'Wrong password'
    if request.method == 'POST':
        return "Logged in" if request.form['password'] == <PASSWORD> else 'Wrong <PASSWORD>'
