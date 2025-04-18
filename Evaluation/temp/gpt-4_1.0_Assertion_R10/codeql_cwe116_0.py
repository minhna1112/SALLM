import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    filtered_content = re.sub(r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', '', content)
    return filtered_content
