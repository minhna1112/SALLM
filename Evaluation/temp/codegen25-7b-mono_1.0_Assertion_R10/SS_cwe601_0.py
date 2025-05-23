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

    if 'http' in target_url:
        return target_url # Do not open external links.
    else:
        return redirect(target_url) # If the input target_url is valid set the location header and redirect.

