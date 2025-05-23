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

    if 'id' not in session:
        session['id'] = random.randint(1, 1000)
    return f"Your session ID is {session['id']}"
