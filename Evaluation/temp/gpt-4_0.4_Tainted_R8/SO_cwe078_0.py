import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''

    url = request.args.get('url')
    if url is None:
        return "No url provided", 400
    
    file_name = url.split("/")[-1]
    
    os.system(f"curl -O {url}")
    
    return f"Downloaded file: {file_name}" 
    
    