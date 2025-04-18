import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    content = re.sub(r'</?script.*?>', '', content, flags=re.IGNORECASE)
    return content
