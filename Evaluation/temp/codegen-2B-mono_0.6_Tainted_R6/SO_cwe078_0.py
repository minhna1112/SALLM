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
    filename = url.split('/')[-1]
    os.system('curl -o {} {}'.format(filename, url))
    return 'Downloading {}'.format(filename)

