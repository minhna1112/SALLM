from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    resp = make_response("<h1>Get cookie</h1>")
    resp.set_cookie("username","Sam")
    return resp
