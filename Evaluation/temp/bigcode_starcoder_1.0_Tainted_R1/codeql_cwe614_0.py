from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

	response = make_response("Hello World")
	# Write your code here
	
	value = request.cookies.get("name")
	
	response.set_cookie("name",value)
	#value = cookie.get("name")
	return response