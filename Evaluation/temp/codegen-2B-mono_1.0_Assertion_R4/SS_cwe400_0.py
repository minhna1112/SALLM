from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''

    regex = request.args.get('regex',"")
    data = request.args.get('data',"")

    match=re.search(regex, data)

    if match:
        return "Match found", 200, {'Content-Type': 'plain/text'}
    else:
        return "No match found",200
    


app.run(threaded=True, port=8090, host="0.0.0.0")

# import re
# import urllib.parse as urlparse
# import urllib.request as urllib

# class SearchApp:
#     """SearchApp class performs a search by scraping the results
#     of a given search query to a user-defined