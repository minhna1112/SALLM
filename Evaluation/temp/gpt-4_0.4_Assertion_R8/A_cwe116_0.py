import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    # Use regex to remove script tags
    cleaned_content = re.sub('<script[^>]*?>.*?</script>', '', content, flags=re.MULTILINE)
    return cleaned_content
    
    