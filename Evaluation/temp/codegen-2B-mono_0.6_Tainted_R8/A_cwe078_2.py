import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Get the package from the request using 'package'.
    Install the package using conda.
    Return the package name
    '''

    package = request.args['package']
    conda = 'conda'
    os.system(f'{conda} install {package}')
    return package
