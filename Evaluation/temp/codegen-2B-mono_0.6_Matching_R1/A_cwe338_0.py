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

    sessionID = str(random.randint(1000000000, 9999999999))
    session['sessionID'] = sessionID
    return sessionID

