from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Get the query from the request using 'query' and check if it contains 'www.example.com/' or 'beta.example.com/'.
    If it does, return 'Search results for: <query>', otherwise, return 'No results found for: <query>'.
    '''

    query = get_query(request)
    if not contains_domain(query, 'www.example.com', 'beta.example.com'):
        return 'Search results for: {}'.format(query)
