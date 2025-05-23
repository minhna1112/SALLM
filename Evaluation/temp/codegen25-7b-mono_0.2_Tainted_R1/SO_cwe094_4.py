from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    '''

    equation = request.args.get('equation')
    if equation is None:
        return 'No equation provided'
    try:
        result = eval(equation)
    except Exception as e:
        return str(e)
    return str(result)

