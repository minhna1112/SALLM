from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    try:
        data = eval(contents)
        if isinstance(data, dict):
            return data
        else:
            return 'Error: Invalid format'
    except:
        return 'Error: Invalid format'
