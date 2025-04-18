from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    if formattedStr :
        formattedStr = formattedStr.replace(' ', '')
        formattedStr = formattedStr.replace('\n', '')
        formattedStr = formattedStr.replace('\t', '')
        formattedStr = formattedStr.replace('\r', '')
        formattedStr = formattedStr.replace('\r\n', '')
        formattedStr = formattedStr.replace('\r', '')
        formattedStr = formattedStr.replace('\n', '')
        formattedStr = formattedStr.replace('\t', '')
        formattedStr = formattedStr.replace('\r', '')
        formattedStr = formattedStr.replace('\n', ''