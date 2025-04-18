from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args['file_contents']
    if file_contents[0] == '{' and file_contents[len(file_contents)-1] == '}':
        file_contents = file_contents[1:(len(file_contents)-1)]
    return eval(file_contents)
app.run()
