from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = str(request.args.get('code', ''))
    out = __execute_code(code)
    return out

