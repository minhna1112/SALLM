import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext
