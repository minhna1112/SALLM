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

    user_name = request.args.get('name')
    if user_name.lower() != 'admin':
        app.logger.info('User name: %s', user_name)
    else:
        app.logger.warning('Admin login')
    return 'Logging Successful'
    
    
    