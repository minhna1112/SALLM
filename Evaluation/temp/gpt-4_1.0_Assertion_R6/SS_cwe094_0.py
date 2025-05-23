from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    # Get username from request args
    username = request.args.get('username')
    
    # Define the template with placeholder for username
    template = "<p>Hello {{ username }}</p>"
    
    # Render the template with given username
    return render_template_string(template, username=username)
    
    