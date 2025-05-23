from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

    name = request.args.get('name')
    print(name)
    if name == 'admin':
        return '<h1>Hello Admin, this is your name: {}</h1>'.format(name)
    else:
        return '<h1>Hello User, this is your name: {}</h1>'.format(name)
