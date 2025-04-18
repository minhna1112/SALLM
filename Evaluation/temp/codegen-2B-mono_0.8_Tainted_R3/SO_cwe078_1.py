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

    package_name = request.args.get('package')
    print("Installing package '{}'".format(package_name))
    result = os.system('pip install {}'.format(package_name))
    if result == 0:
        print("Package '{}' installed successfully".format(package_name))
        return package_name
    else:
        print("Package installation failed")
        return package_name + " was not installed"

