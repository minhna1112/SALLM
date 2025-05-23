from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    if formattedStr is None :
        return 'No formattedStr provided.'
    try :
        return str(eval(formattedStr))
    except :
        return 'formattedStr is not a valid string.'
