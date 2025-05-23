from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    str_var = request.args.get('str_var')
    try:
        var = int(str_var)
    except ValueError:
        try:
            var = float(str_var)
        except ValueError:
            var = str(str_var)
    return var

