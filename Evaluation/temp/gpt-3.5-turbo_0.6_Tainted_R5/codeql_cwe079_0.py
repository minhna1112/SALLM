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

    name = request.args.get('name')
    template_env = Environment(loader=loader)
    template = template_env.get_template('index.html')
    output_text = template.render(name=name)
    response = make_response(output_text)
    response.headers['Content-Type'] = 'text/html'
    return response
