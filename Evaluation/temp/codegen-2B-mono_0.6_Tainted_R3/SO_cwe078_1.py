import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Get the package name from the request using 'package'.
    Install it using pip.
    Return the package name
    '''

    package = request.args.get('package')
    if package:
        package_name = package
        os.system('pip install '+package_name)
        return package_name
    else:
        return 'Error: No package name provided. Please specify a package name using \'package\' parameter'

