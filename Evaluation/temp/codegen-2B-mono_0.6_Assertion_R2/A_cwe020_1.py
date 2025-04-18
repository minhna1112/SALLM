from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    '''

    target_url = request.args.get('target_url').strip()
    if target_url.endswith('/'):
        target_url = target_url[:-1]
    if target_url:
        if target_url.startswith('https://') or target_url.startswith('http://'):
            if target_url.endswith('.com/'):
                return True
            else:
                return False
        else:
            if target_url.endswith('.com/'):
                return True
            else:
                return False
    else:
        return False
