from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # Get param from request.
    param = request.args.get('param')
    # Replace param in template.
    with open('../assets/templates/template.html', 'r') as f:
        content = f.read()
        content = content.replace('$$$', param)
        return content
