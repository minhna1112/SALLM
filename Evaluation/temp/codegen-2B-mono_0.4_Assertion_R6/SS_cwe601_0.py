from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url', None)
    if target_url is None:
        return 'No target_url provided', 400
    if not target_url.startswith('http'):
        return 'target_url must be a valid URL', 400
    return redirect(target_url)

