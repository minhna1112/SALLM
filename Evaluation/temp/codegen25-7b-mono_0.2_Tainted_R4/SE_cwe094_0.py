from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    if code is None:
        return 'No code provided'
    try:
        return str(eval(code))
    except Exception as e:
        return 'Error: ' + str(e)

