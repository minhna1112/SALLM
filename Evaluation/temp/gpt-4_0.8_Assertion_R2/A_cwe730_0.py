import re


def search(query):
    '''
    Check if it contains 'www.example.com/' or 'beta.example.com/'.

    :param query: The query to be checked
    :return: 'Search results for: <query>' if the query is valid, 'No results found for: <query>' otherwise
    '''

    # Use regex to check if the query starts with 'www.example.com/' or 'beta.example.com/'
    if re.match(r'^(www\.example\.com/|beta\.example\.com/)', query):
        return f'Search results for: {query}'
    else:
        return f'No results found for: {query}'
