from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    res = Response(response="Hello, Flask!\n", status=200, mimetype="text/plain")
    res.headers['Content-Type'] = 'text/plain'
    return res
