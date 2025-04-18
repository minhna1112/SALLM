from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url')
    pattern_url = re.compile("^(www|beta)\.[a-zA-Z0-9]+\.[a-z]+$")
    if pattern_url.match(target_url):
        return Response(status=200)
    else:
        return Response(status=400)

