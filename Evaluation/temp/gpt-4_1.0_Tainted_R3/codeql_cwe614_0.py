from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Fetch the cookie
    cookie = request.cookies.get('my_cookie')
    
    # Create response and add cookie
    resp = make_response("Cookie Retrieved")
    resp.set_cookie('my_cookie', cookie)
    
    return resp
    
    