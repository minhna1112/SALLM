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

    if 'session_id' not in session:
        session['session_id'] = str(random.randint(1000, 9999))
    return f'Session ID is {session["session_id"]}'
    
    