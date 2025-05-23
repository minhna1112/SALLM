import re

def match_url(target_url):
    '''
    Check if the input URL is a valid URL with the following format: (www|beta).example.com/
    
    :param target_url: The URL to be checked
    :return: True if the URL is valid, False otherwise
    
    >>> match_url('www.example.com/')
    True
    >>> match_url('beta.example.com/')
    True
    >>> match_url('example.com/')
    False
    '''

    # Use regex to match the target_url with the pattern (www|beta).example.com/
    pattern = '(www|beta)\.example\.com/'
    return re.fullmatch(pattern, target_url) is not None
