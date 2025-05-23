import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    if command =='move':
        return 'Moving'
    elif command == 'turnLeft':
        return 'Turning Left'
    elif command == 'turnRight':
        return 'Turning Right'
    else:
        return 'Command Not Found!'
