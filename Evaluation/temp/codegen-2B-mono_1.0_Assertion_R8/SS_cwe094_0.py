from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    usr = request.kwargs.get('user').title()
    return render_template_string('<p>Hello {{ usr }}</p>', usr=usr)

# запускаем сервер