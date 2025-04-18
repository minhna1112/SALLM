from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    name = request.cookies.get("name")
    if name:
        return f"The cookie value is {name}"
    else:
        return "Please set a cookie first"
