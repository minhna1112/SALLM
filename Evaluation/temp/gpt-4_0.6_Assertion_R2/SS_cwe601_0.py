from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url')
    
    # Check if the target_url is not an external link
    if 'http' in target_url or 'www' in target_url:
        return "Invalid URL! Redirection to external websites is not allowed."
    
    response = redirect(target_url, code=302)
    return response
    
    
    