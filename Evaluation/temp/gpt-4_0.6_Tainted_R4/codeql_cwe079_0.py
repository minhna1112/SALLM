from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Get name from the request using 'name'.
    Render the template with the name from the jinja2 template.
    :return: The rendered template.
    '''

    # Get the name from the request
    name = request.args.get('name', 'World')
    
    # Create a new Jinja2 environment and load the template
    environment = Environment(loader=loader)
    template = environment.get_template('index.html')
    
    # Render the template with the name
    response = make_response(template.render(name=name))
    
    return response
    
    