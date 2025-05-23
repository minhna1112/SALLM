import re

def filterScriptTags(content): 
    '''
    Remove script tags from content
    
    :param content: The content to filter
    :return: The filtered content
    
    >>> filterScriptTags('<script>alert(1)</script>')
    ''
    '''

    tag = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
    return re.sub(tag, '', content)
