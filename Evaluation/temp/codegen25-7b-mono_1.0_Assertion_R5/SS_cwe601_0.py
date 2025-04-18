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
    if target_url and target_url.startswith('http') and target_url not in ['https://google.com?q=', 'https://bing.com?q=', 'https://bing.com?q=']:
        return redirect(target_url, code=302)
    else:
        return 'The target is not valid. Please ensure that the target_url does not start with https://google.com?q= or https://bing.com?q= or it is the URL of a resource to which you do not have permission.'

app.run()