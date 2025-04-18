import re

def match_string(target_string):
    '''
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''

    if not isinstance(target_string, str):
        return False
    if target_string == '':
        return False
    if len(target_string.split('.'))!= 3:
        return False
    for i in range(len(target_string.split('.'))):
        if not re.match('^[a-zA-Z0-9]+$', target_string.split('.')[i]):
            return False
    return True
