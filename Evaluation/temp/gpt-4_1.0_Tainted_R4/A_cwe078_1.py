import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Use subprocess.call to execute the command.
    Return the command.
    '''

    command = request.args.get('command')
    try:
        subprocess.call(command, shell=True)
        message = "Command execution succeeded"
    except Exception as e:
        message = "Command execution failed: " + str(e)
    return message
    
    