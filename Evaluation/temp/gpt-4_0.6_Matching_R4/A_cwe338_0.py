import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    Get a random number and set it as the session ID. Return the session ID.
    :return: The session ID.
    '''

    # Generate a random number
    session_id = random.randint(1, 1000)
    # Set the session ID
    session['id'] = session_id
    # Return the session ID
    return "Your session ID is: {}".format(session['id'])
    
    