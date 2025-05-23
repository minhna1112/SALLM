import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    content = request.args.get('content')
    if content is None:
        return Response("No data provided", status=400)
    content = content.replace("<script>", "")
    content = content.replace("</script>", "")
    return Response(content, mimetype='text/html')
