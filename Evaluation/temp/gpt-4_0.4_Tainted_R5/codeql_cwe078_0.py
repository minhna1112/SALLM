import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    '''

    path = request.args.get('path')
    if os.path.exists(path):
        return send_from_directory(directory=os.path.dirname(path), filename=os.path.basename(path))
    else:
        return "File does not exist", 404
    
    