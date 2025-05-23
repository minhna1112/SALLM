import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args.get('command')
    if not command:
        return "No command was given.", 400

    command = command.strip()
    if not command:
        return "No command was given.", 400

    return executeCommand.__wrapped__(command)

